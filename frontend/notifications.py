import time, datetime, pytz
import Constants as keys
import requests
import globals

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
    print('hello world')
    ## Scrape data here
    email_array = ["hello world", "hello one"]
    for email in email_array:
        context.job.context.effective_user.send_message(text=email)
