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
    interval = globals.frequency * 60 * 60

    remove_job(str(chat_id), context) #remove any existing jobs
    time_zone = pytz.timezone("Asia/Singapore")
    context.job_queue.run_repeating(send_notification, interval, context=update)

def send_notification(context):
    email_addresses = globals.email_address
    passwords = globals.passwords
    for i in len(email_addresses):
        email_array = backend.scrape(email_addresses[i], passwords[i], globals.frequency, globals.last_query, globals.keywords)

    globals.last_query = datetime.now()
    for email in email_array:
        context.job.context.effective_user.send_message(text=email)