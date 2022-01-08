import pytz
from datetime import datetime, timedelta
import Constants as keys
import requests
import globals
import backend

def remove_job(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return 
    for job in current_jobs:
        job.schedule_removal()

def off_notif(update, context):
    query = update.callback_query
    chat_id=query.message.chat_id
    
    remove_job(str(chat_id), context)

def on_notif(update, context):
    query = update.callback_query
    chat_id=query.message.chat_id
    interval = globals.frequency[chat_id] * 60 * 60
    print(interval)

    remove_job(str(chat_id), context) #remove any existing jobs
    # time_zone = pytz.timezone("Asia/Singapore")
    context.job_queue.run_repeating(send_notification, 30, context=update)

def send_notification(context):
    query = context.job.context.callback_query
    chat_id = query.message.chat_id
    print(chat_id)
    email_addresses = globals.email_address[chat_id]
    passwords = globals.password[chat_id]

    if chat_id in globals.keywords:
        keywords = globals.keywords[chat_id]
    else:
        keywords = []

    for i in range(len(email_addresses)):
        email_array = backend.scrape(email_addresses[i], passwords[i], globals.frequency[chat_id], globals.last_query[chat_id], keywords)

    globals.last_query[chat_id] = datetime.now()
    for email in email_array:
        context.job.context.effective_user.send_message(text=email)