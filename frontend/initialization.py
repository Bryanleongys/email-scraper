from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import keyboards


def start(update, context):
    chat_id = update.message.chat.id
    username = str(update.message.from_user.username)

    text = "Hi @" + username + "! Let's get you started!"
    text2 = "May I know your email address?"

    update.message.reply_text(text)
    update.message.reply_text(text2)

    return 1

def get_email(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text

    text = "Your email " + user_input + " has been registered."
    text2 = "Please enter the password to the email given."

    update.message.reply_text(text)
    update.message.reply_text(text2)

    return 2

def get_password(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text
    ## Authentication if password is invalid - input conditional statement
    if (False):
        update.message.reply_text(
            text="Invalid password. Please re-type your email and password."
        )
        return 1

    text = "Your password " + user_input + " has been stored."

    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Frequency tabs."

    update.message.reply_text(text)
    update.message.reply_text(text2)

    return ConversationHandler.END