from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import keyboards
import re
import backend
import globals

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False

def start(update, context):
    chat_id = update.message.chat.id
    username = str(update.message.from_user.username)

    text = "Hi @" + username + "! Let's get you started!"
    text2 = "May I know your email address?"

    update.message.reply_text(text)
    update.message.reply_text(text2)

    return 1

def add_email(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    text = "Following are your current email addresses, click to remove, and type in to add a new email."

    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.email_keyboard()
    )

    return 1

def delete_email(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    query = update.callback_query
    index = int(query.data[5:])

    if (len(globals.email_address) == 1):
        text = "Please keep at least one email stored."
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
        )
        text2 = "Following are your current email addresses, click to remove, and type in to add a new email."
        context.bot.send_message(
            chat_id=chat_id,
            text=text2,
            reply_markup=keyboards.email_keyboard()
        )
    
    else:
        del globals.email_address[index]

        text = "Following are your current email addresses, click to remove, and type in to add a new email."
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            reply_markup=keyboards.email_keyboard()
        )

    return 1

def get_email(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text
    context.user_data["email_address"] = user_input

    if not isValid(user_input):
        text = "Your email " + user_input + " is invalid."
        text2 = "Please enter your email again."

        update.message.reply_text(text)
        update.message.reply_text(text2)

        return 1
    else:
        text = "Your email " + user_input + " has been registered."
        text2 = "Please enter the password to the email given."
    
        update.message.reply_text(text)
        update.message.reply_text(text2)

        return 2


def get_password(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text
    ## Authentication if password is invalid - input conditional statement
    ## Backend functions to login to email
    email_address = context.user_data["email_address"]
    print(email_address)
    print(user_input)

    if not (backend.authenticate(email_address, user_input)):
        update.message.reply_text(
            text="Invalid password. Please re-type your email and password."
        )
        return 1

    globals.email_address.append(email_address)
    globals.password.append(user_input)

    print(globals.email_address)
    print(globals.password)

    text = "Your password " + user_input + " has been stored."

    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."

    update.message.reply_text(text)
    update.message.reply_text(text=text2, reply_markup=keyboards.main_options_keyboard())

    return ConversationHandler.END