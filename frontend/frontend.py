from telegram.ext import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton, Message, Bot, ReplyKeyboardRemove
from functools import partial
import Constants as keys

def error(update, context):
    print("error")

def main():
    updater = Updater(keys.API_KEY)
    dp = updater.dispatcher
    