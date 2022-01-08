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
    if chat_id in globals.email_address:
        email_addresses = globals.email_address[chat_id]
    else:
        return
    
    if chat_id in globals.password:
        passwords = globals.password[chat_id]
    else:
        return
        
    if chat_id in globals.keywords:
        keywords = globals.keywords[chat_id]
    else:
        keywords = []
    # for i in range(len(email_addresses)):
    #     text_messages = backend.scrape(email_addresses[i], passwords[i], globals.frequency, globals.last_query, globals.keywords)
    for i in range(len(email_addresses)):
        text_messages = backend.scrape(email_addresses[i], passwords[i], globals.frequency[chat_id], globals.last_query[chat_id], keywords)
        for text in text_messages:
            context.bot.send_message(
            chat_id=chat_id,
            text=text,
            )
            
    globals.last_query[chat_id] = datetime.now()

 
    
    text2 = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."
    context.bot.send_message(
        chat_id=chat_id,
        text=text2,
        reply_markup=keyboards.main_options_keyboard()
    )

    return ConversationHandler.END