from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals

def main_options_keyboard():
    keyboard = [
        [InlineKeyboardButton(
            "Keywords", callback_data='keywords')],
        [InlineKeyboardButton("Message Settings", callback_data='message_settings')],
        [InlineKeyboardButton("Check Messages", callback_data='check_messages')],
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

