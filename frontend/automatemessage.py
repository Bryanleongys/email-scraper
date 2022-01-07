import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals
import time, datetime, pytz
import notifications

def prompt_automate(update, context):
   
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    text = "Please select to on or off your automated messages."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.automate_keyboard()
    )

    return 1

def select_automate(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    globals.automate = not globals.automate

    if (globals.automate):
        notifications.on_notif(update, context)
        text = "Automated messages are currently turned on."
    else:
        notifications.off_notif(update, context)
        text = "Automated messages are currently turned off."

    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
    )
    context.bot.send_message(
        chat_id=chat_id,
        text=text2,
        reply_markup=keyboards.main_options_keyboard()
    )

    return ConversationHandler.END