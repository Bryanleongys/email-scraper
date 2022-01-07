
import time, datetime, pytz

global frequency
frequency = 24
global keywords
keywords = []

global email_address
email_address = ""
global password
password = ""

global automate
automate = False

global last_query
time_zone = pytz.timezone("Asia/Singapore")
last_query = datetime.time(hour=0, minute=0, second=0, tzinfo=time_zone)