import time, datetime, pytz

global frequency
frequency = 24
global keywords
keywords = {}

global email_address
email_address = []
global password
password = []

global automate
automate = False

global last_query
time_zone = pytz.timezone("Asia/Singapore")
last_query = datetime.datetime(year = 1999, month = 1, day = 1, hour = 0, minute = 0, second = 0)