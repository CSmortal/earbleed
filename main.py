import os
import telebot
import emoji
from dotenv import load_dotenv
from apply_audio_fx import effect_audio
from constants import *

USR_VOX_MSG = None
TEMP_FILE_PROCESSED = "./temp-fx.ogg"

load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_greeting(message):
    bot.send_message(message.chat.id, "Hello! I can change the voice and add various effects to it")

@bot.message_handler(func=lambda message: message.text == "reset", content_types=['text'])
def reset(message):
    global USR_VOX_MSG
    USR_VOX_MSG = None
    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Please send another audio clip...", reply_markup=markup)

@bot.message_handler(content_types=['audio', 'voice'])
def handle_voice_file(message):
        global USR_VOX_MSG
        if USR_VOX_MSG == None:
            USR_VOX_MSG = message.voice.file_id
            #bot.send_voice(message.chat.id, message.voice.file_id)
    
            # add buttons for the user to select the audio effect he/she desires
            markup = telebot.types.ReplyKeyboardMarkup()

            itemDeep = telebot.types.KeyboardButton('Deep')
            itemChipmunk = telebot.types.KeyboardButton('Chipmunk')
            itemReverse = telebot.types.KeyboardButton('Reverse')
            itemEcho = telebot.types.KeyboardButton('Echo')
            itemDrunk = telebot.types.KeyboardButton('Drunk')
            itemDeepFried = telebot.types.KeyboardButton('Deep Fried')
            itemReset = telebot.types.KeyboardButton('reset')

            markup.row(itemDeep, itemChipmunk)
            markup.row(itemReverse, itemEcho)
            markup.row(itemDrunk, itemDeepFried)
            markup.row(itemReset)

            # depending on audio effect selection, send the processed voice file back to user
            bot.send_message(message.chat.id, "Choose the audio effect you would like to add", reply_markup=markup)

def common_reply(message, reply):
    bot.send_message(message.chat.id, reply) 
    voice = open(TEMP_FILE_PROCESSED, 'rb')
    bot.send_voice(message.chat.id, voice)
    reset(message)

@bot.message_handler(func=lambda message: message.text == "Deep", content_types=['text'])
def handle_deep(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, DEEP)
        common_reply(message, "INTO THE DEEEEEEEEEEEEEEEEEEEEEP")

@bot.message_handler(func=lambda message: message.text == "Chipmunk", content_types=['text'])
def handle_chipmunk(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, CHIPMUNK)
        common_reply(message, "Here you go, you chipmunk")

@bot.message_handler(func=lambda message: message.text == "Reverse", content_types=['text'])
def handle_reverse(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, REVERSE)
        common_reply(message, "gnidrocer rouy si ereH")

@bot.message_handler(func=lambda message: message.text == "Echo", content_types=['text'])
def handle_echo(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, ECHO)
        common_reply(message, "Here here is is your your recording recording")

@bot.message_handler(func=lambda message: message.text == "Drunk", content_types=['text'])
def handle_drunk(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, DRUNK)
        common_reply(message, "heRe iS yOUr REc0oo..rrDiNg")

@bot.message_handler(func=lambda message: message.text == "Deep Fried", content_types=['text'])
def handle_deepfried(message):
    global USR_VOX_MSG
    if not USR_VOX_MSG == None:
        effect_audio(USR_VOX_MSG, API_KEY, ECHO)
        common_reply(message, "!!!HEREISYOURRECORDING!!!")
    
bot.infinity_polling()
