from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals

def main_options_keyboard():
    keyboard = [
        [InlineKeyboardButton(
            "Keywords", callback_data='keywords')],
        [InlineKeyboardButton("Message Settings", callback_data='message_settings')],
        [InlineKeyboardButton("Check Messages", callback_data='check_messages')],
        [InlineKeyboardButton("Change Password", callback_data="change_password")],
        [InlineKeyboardButton("Emails", callback_data="add_email")],
    ]
    return InlineKeyboardMarkup(keyboard)

def keyword_keyboard(chat_id):
    if chat_id in globals.keywords:
        keywords = globals.keywords[chat_id] 
    else:
        keywords = []
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
    keyboard.append([InlineKeyboardButton("Back", callback_data="back_message_settings")])
    return InlineKeyboardMarkup(keyboard)

def message_settings_keyboard():
    keyboard = []
    keyboard.append([InlineKeyboardButton("Frequency", callback_data="frequency")])
    keyboard.append([InlineKeyboardButton("On/Off Automated Messaging", callback_data="automate_messaging")])
    keyboard.append([InlineKeyboardButton("Back", callback_data="go_back_home")])
    return InlineKeyboardMarkup(keyboard)

def automate_keyboard():
    keyboard = []
    if (globals.automate):
        keyboard.append([InlineKeyboardButton("Off", callback_data="on_off")])
    else:
        keyboard.append([InlineKeyboardButton("On", callback_data="on_off")])

    keyboard.append([InlineKeyboardButton("Back", callback_data="back_message_settings")])
    return InlineKeyboardMarkup(keyboard)

def email_keyboard(chat_id):
    keyboard = []
    if chat_id in globals.email_address:
        email_addresses = globals.email_address[chat_id]
    else:
        email_addresses = []
    counter = 0
    for email_address in email_addresses:
        keyboard.append([InlineKeyboardButton(email_address, callback_data=("email"+str(counter)))])
        counter += 1
    
    keyboard.append([InlineKeyboardButton("Back", callback_data="main_options")])

    return InlineKeyboardMarkup(keyboard)