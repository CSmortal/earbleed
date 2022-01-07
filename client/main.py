import os
import telebot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_greeting(message):
    bot.send_message(message.chat.id, "Hello! I can change the voice and add various effects to it")


bot.polling()