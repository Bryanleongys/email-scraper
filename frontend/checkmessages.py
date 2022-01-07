import keyboards
import initialization
from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
import globals

def send_message(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    ## Scraper function here
    text_messages = ["Date: 2022-01-07 13:39 SGT\nSubject: this is a test email\nFrom: sandboxreply@gmail.com\nHi Im back.\r\n    \r\n    Best regards,\r\n    Im back\r\n\n", "hello1", "hello2"]

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