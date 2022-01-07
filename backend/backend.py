import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from datetime import datetime, timedelta

previous_query_time = datetime.now() - timedelta(hours = 1)
print(previous_query_time)

# user login
try:
    user_email = "noreplytest2468@gmail.com"
    user_password = "A12345678!"
except:
    print('good try')
else:
    pass
#finally:

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
def authenticate(user_email, user_password):
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(user_email, user_password)
    except:
        return 'authentication failed'
    else:
        return 'authentication success'

#scrape
def scrape(user_email, user_password, N, last_query, keywords):
    previous_query_time = datetime.now()
    if (datetime.now() - last_query < timedelta(hours = N)):
        previous_query_time = last_query
    else:
        previous_query_time = (datetime.now() - timedelta(hours = N))
    print(previous_query_time)
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(user_email, user_password)
    except:
        return 'authentication failed'
    else:
        status, messages = imap.select("INBOX")
        messages = int(messages[0])

        break_flag = False
        result = ""
        while(break_flag != True):
            # fetch the email message by ID
            res, msg = imap.fetch(str(messages), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    # Thu, 06 Jan 2022 08:58:39 -0800 (PST)
                    email_date = msg['Date']
                    email_array = email_date.split(" ")
                    email_year = int(email_array[3])
                    month_name = email_array[2]
                    datetime_object = datetime.strptime(month_name, "%b")
                    email_month = datetime_object.month
                    email_day = int(email_array[1])
                    email_hour = int(email_array[4][:2])
                    email_minute = int(email_array[4][3:5])
                    email_date_object = datetime(email_year, email_month, email_day, email_hour, email_minute) + timedelta(hours = 16)
                    if (email_date_object < previous_query_time):
                        break_flag = True
                        break
                    result += ("Date: " + email_date_object.strftime("%Y-%m-%d %H:%M") + " SGT\n")
                    # print("Date:", email_date_object.strftime("%Y-%m-%d %H:%M"), "SGT") 
                    result += ("Subject: " + subject + "\n")
                    # print("Subject:", subject)
                    result += ("From: " + From + "\n")
                    # print("From:", From)

                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                result += (body[:160] + "\n")
                                # print(body)
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            result += (body[:160] + "\n")
                            # print(body)
                    result += (("="*100) + "\n")       
                    # print("="*100)
            messages -= 1
        # close the connection and logout
        imap.close()
        imap.logout()
        return result

print(scrape("noreplytest2468@gmail.com", "A12345678!", 3, datetime.now() - timedelta(hours=2), "hello"))

    