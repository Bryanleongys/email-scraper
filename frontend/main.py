from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
from functools import partial
import Constants as keys
import initialization

def error(update, context):
    print("error")

def main():
    updater = Updater(keys.API_KEY)
    dp = updater.dispatcher

    dp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("start", initialization.start)],
            states={
                1: [MessageHandler(Filters.text, initialization.get_email)],
                2: [MessageHandler(Filters.text, initialization.get_password)],
            },
            fallbacks=[],
            per_user=False
        )
    )

    updater.start_polling()
    updater.idle()


main()