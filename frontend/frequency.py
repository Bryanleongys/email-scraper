import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals


def prompt_frequency(update, context):
   
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    text = "Please click on the time interval you would like me to check your email"
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.frequency_keyboard()
    )

    return 1

def select_frequency(update, context):
    
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    text = "Please click on the time interval you would like me to check your email"
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.frequency_keyboard()
    )

    return 1
