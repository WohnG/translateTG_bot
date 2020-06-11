import telebot
import googletrans
from googletrans import Translator
import config

bot = telebot.TeleBot(config.TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот-переводчик с любого языка на английский, введи слово или фразу - и я переведу её! \n /help - список поддерживающихся языков")

@bot.message_handler(commands=['help'])
def send_help(message):
    suppot_langs = googletrans.LANGUAGES
    x = ''
    for key, value in suppot_langs.items():
        x += key + ' - ' + value + '\n'
    bot.reply_to(message, x)

@bot.message_handler(content_types=['text'])
def tr_eng(message):
    result = translator.translate(message.text)
    bot.reply_to(message, result.text)

bot.polling()


