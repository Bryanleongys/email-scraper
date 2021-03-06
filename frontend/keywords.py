import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals

def prompt_keywords(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    text = "Following are the keywords you have added. Type to add in a new keyword, click to delete a keyword."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.keyword_keyboard(chat_id)
    )

    return 1

def add_keyword(update, context):
    chat_id = update.message.chat.id
    user_input = update.message.text
    if chat_id in globals.keywords:
        globals.keywords[chat_id].append(user_input)
    else:
        globals.keywords[chat_id] = [user_input,]
    
    print(globals.keywords)
    
    text = "Keyword added!"
    text2 = "Following are the keywords you have added. Type to add in a new keyword, click to delete a keyword."
    update.message.reply_text(text=text)
    update.message.reply_text(
        text=text2, reply_markup=keyboards.keyword_keyboard(chat_id))

    return 1

def delete_keyword(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    query = update.callback_query
    index = int(query.data[4:])

    del globals.keywords[chat_id][index]

    text = "Following are the keywords you have added. Type to add in a new keyword, click to delete a keyword."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.keyword_keyboard(chat_id)
    )

    return 1
