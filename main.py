import os
import telebot
import emoji
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_greeting(message):
    bot.send_message(message.chat.id, "Hello! I can change the voice and add various effects to it")


@bot.message_handler(content_types=['audio', 'voice'])
def handle_voice_file(message):

    bot.send_voice(message.chat.id, message.voice.file_id)
    
    # add buttons for the user to select the audio effect he/she desires
    markup = types.ReplyKeyboardMarkup()

    itemPitchIncr = types.KeyboardButton('Pitch Up')
    itemPitchDecr = types.KeyboardButton('Pitch Down')

    markup.row(itemPitchIncr, itemPitchDecr)

    bot.send_message(message.chat.id, "Choose the audio effect you would like to add", reply_markup=markup)

    # depending on audio effect selection, send the processed voice file back to user
    

bot.infinity_polling()