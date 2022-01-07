from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals

def main_options_keyboard():
    keyboard = [
        [InlineKeyboardButton(
            "Keywords", callback_data='keywords')],
        [InlineKeyboardButton("Message Settings", callback_data='message_settings')],
    ]
    return InlineKeyboardMarkup(keyboard)

def keyword_keyboard():
    keywords = globals.keywords 
    keyboard = []
    counter = 0
    for keyword in keywords:
        keyboard.append([InlineKeyboardButton(keyword, callback_data=("word"+str(counter)))])
        counter += 1

    keyboard.append([InlineKeyboardButton("Back", callback_data="main_options")])
    return InlineKeyboardMarkup(keyboard)

def frequency_keyboard():
    # intervals = [12,24]#in hours
    keyboard = []
    keyboard.append([InlineKeyboardButton("12h", callback_data="interval12")])
    keyboard.append([InlineKeyboardButton("24h", callback_data="interval24")])
    keyboard.append([InlineKeyboardButton("Back", callback_data="main_options")])
    return InlineKeyboardMarkup(keyboard)

def message_settings_keyboard():
    keyboard = []
    keyboard.append([InlineKeyboardButton("Frequency", callback_data="frequency")])
    keyboard.append([InlineKeyboardButton("Check Email Now", callback_data="check_email")])
    keyboard.append([InlineKeyboardButton("Back", callback_data="main_options")])
    return InlineKeyboardMarkup(keyboard)