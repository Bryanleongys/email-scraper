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
    query = update.callback_query
    interval = int(query.data[8:])
    globals.frequency = interval

    text = f'Messages will be sent every {interval} hours'

    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.main_options_keyboard()
    )
    return ConversationHandler.END


def prompt_message_setting(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    text = "Adjust the reminder interval here, or on/off automated messaging."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.message_settings_keyboard()
    )

    return ConversationHandler.END

def check_email(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    text = "This function requires professionals to edit. Development in Progress..."
    # context.bot.edit_message_text(
    #     chat_id=chat_id,
    #     message_id=message_id,
    #     text=text,
    #     reply_markup=keyboards.frequency_keyboard()
    # )

    update.message.reply_text(text)

    return ConversationHandler.END