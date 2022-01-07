import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals
import backend

def select_email(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    text = "Please select the email you would like to change your password."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.email_keyboard()
    )

    return 1

def prompt_password(update, context):
    query = update.callback_query
    index = int(query.data[5:])
    email_address = globals.email_address ## change to globals.email_address[index]
    context.user_data["email_address"] = email_address
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    text = "Please enter your new password."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
    )

    return 2

def confirm_password(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text

    email_address = context.user_data["email_address"]

    if not (backend.authenticate(email_address, user_input)):
        update.message.reply_text(
            text="Invalid password. Please re-type your password."
        )
        return 2

    globals.password = user_input

    text = "Your password " + user_input + " has been updated."

    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."

    update.message.reply_text(text)
    update.message.reply_text(text=text2, reply_markup=keyboards.main_options_keyboard())

    return ConversationHandler.END


