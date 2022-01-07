import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals
import backend
from datetime import datetime, timedelta

def send_message(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    
    ## Scraper function here
    text_messages = backend.scrape(globals.email_address, globals.password, globals.frequency, globals.last_query, globals.keywords)
    globals.last_query = datetime.now()

    for text in text_messages:
        context.bot.send_message(
            chat_id=chat_id,
            text=text,
        )
    
    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."
    context.bot.send_message(
        chat_id=chat_id,
        text=text2,
        reply_markup=keyboards.main_options_keyboard()
    )

    return ConversationHandler.END