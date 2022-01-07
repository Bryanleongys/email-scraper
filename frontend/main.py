from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
from functools import partial
import Constants as keys
import initialization
import keywords
import frequency
import keyboards

def error(update, context):
    print("error")

def show_home(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    text = "Welcome to EmailScraper. Please initialize your settings in Keywords and Message Settings tabs."
    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=keyboards.main_options_keyboard()
    )

    return ConversationHandler.END

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

    dp.add_handler(ConversationHandler(
        entry_points=[CallbackQueryHandler(partial(
            keywords.prompt_keywords), pattern="keywords")],
        states={
            1: [MessageHandler(Filters.text, keywords.add_keyword)],
        },
        fallbacks=[CallbackQueryHandler(
            show_home, pattern="main_options"), CallbackQueryHandler(keywords.delete_keyword, pattern="word")],
        per_user=False
    ))
    # dp.add_handler(CallbackQueryHandler(keywords.prompt_frequency, pattern='frequency'))

    updater.start_polling()
    updater.idle()


main()