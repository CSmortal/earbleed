import os
import telebot
import emoji
from dotenv import load_dotenv
from telebot import types

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
    


@bot.message_handler(func=lambda message: message.text == "Pitch Up", content_types=['text'])
def handle_pitch_up(message):

    # do processing

    # send processed file back
    bot.send_message(message.chat.id, "Here is the voice recording but with the pitch increased")
    bot.send_voice(message.chat.id, message.voice.file_id) # replace 2nd argument with either a file_id that exists on tele servers or pass a http url


@bot.message_handler(func=lambda message: message.text == "Pitch Down", content_types=['text'])
def handle_pitch_down(message):

    # do processing

    # send processed file back
    bot.send_message(message.chat.id, "Here is the voice recording but with the pitch decreased")
    bot.send_voice(message.chat.id, message.voice.file_id) # replace 2nd argument with either a file_id that exists on tele servers or pass a http url


bot.infinity_polling()