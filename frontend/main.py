from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
from functools import partial

from telegram.ext import callbackqueryhandler
import Constants as keys
import initialization, keywords, frequency, keyboards, checkmessages, automatemessage, changepassword

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
        fallbacks=[CallbackQueryHandler(show_home, pattern="main_options"), CallbackQueryHandler(keywords.delete_keyword, pattern="word")],
        per_user=False
    ))

    dp.add_handler(CallbackQueryHandler(frequency.prompt_message_setting, pattern='message_setting'))
    dp.add_handler(CallbackQueryHandler(show_home, pattern="go_back_home"))
    
    
    dp.add_handler(ConversationHandler(
        entry_points = [CallbackQueryHandler(frequency.prompt_frequency, pattern='frequency')],

        states={
            1: [CallbackQueryHandler(frequency.select_frequency, pattern="interval")],
        },

        fallbacks=[CallbackQueryHandler(
            frequency.prompt_message_setting, pattern="back_message_settings")],
        per_user=False
        
    
    ))

    dp.add_handler(
        ConversationHandler(
            entry_points=[CallbackQueryHandler(automatemessage.prompt_automate, pattern='automate_messaging')],
            states={
                1: [CallbackQueryHandler(automatemessage.select_automate, pattern="on_off")],
            },
            fallbacks=[CallbackQueryHandler(
            frequency.prompt_message_setting, pattern="back_message_settings")],
            per_user=False
        )
    )

    dp.add_handler(CallbackQueryHandler(checkmessages.send_message, pattern="check_messages"))

    dp.add_handler(
        ConversationHandler(
            entry_points=[CallbackQueryHandler(changepassword.select_email, pattern='change_password')],
            states={
                1: [CallbackQueryHandler(changepassword.prompt_password, pattern="email")],
                2: [MessageHandler(Filters.text, changepassword.confirm_password)],
            },
            fallbacks=[CallbackQueryHandler(show_home, pattern="main_options"), CallbackQueryHandler(
            frequency.prompt_message_setting, pattern="message_settings")],
            per_user=False
        )
    )
    
    dp.add_handler(
        ConversationHandler(
            entry_points=[CallbackQueryHandler(initialization.add_email, pattern="add_email")],
            states={
                1: [MessageHandler(Filters.text, initialization.get_email)],
                2: [MessageHandler(Filters.text, initialization.get_password)],
            },
            fallbacks=[CallbackQueryHandler(show_home, pattern="main_options"), CallbackQueryHandler(initialization.delete_email, pattern="email")],
            per_user=False
        )
    )

    updater.start_polling()
    updater.idle()


main()