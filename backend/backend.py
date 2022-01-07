import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from datetime import datetime, timedelta

previous_query_time = datetime.now() - timedelta(hours = 1)
print(previous_query_time)

def create_email_datetime(email_date):
    email_array = email_date.split(" ")
    email_year = int(email_array[3])
    month_name = email_array[2]
    datetime_object = datetime.strptime(month_name, "%b")
    email_month = datetime_object.month
    email_day = int(email_array[1])
    email_hour = int(email_array[4][:2])
    email_minute = int(email_array[4][3:5])
    email_date_object = datetime(email_year, email_month, email_day, email_hour, email_minute) + timedelta(hours = 16)
    return email_date_object 

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

email_dict = {
    "gmail" : "imap.gmail.com",
    "outlook" : "imap-mail.outlook.com",
    "yahoo" : "imap.mail.yahoo.com",
    "office_365" : "outlook.office365.com",
    "yahoo_plus" : "plus.imap.mail.yahoo.com",
    "mail_com" : "imap.mail.com"
}

def email_sort(user_email):
    if("@gmail" in user_email):
        return "gmail"
    elif("@outlook" in user_email or "@u.nus.edu" in user_email or "@hotmail" in user_email):
        return "outlook"
    elif("@yahoo" in user_email):
        return "yahoo"
    else:
        return "mail_com"

# authenticate
def authenticate(user_email, user_password):
    try:
        imap = imaplib.IMAP4_SSL(email_dict[email_sort(user_email)])
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
        imap = imaplib.IMAP4_SSL(email_dict[email_sort(user_email)])
        imap.login(user_email, user_password)
    except:
        return 'authentication failed'
    else:
        status, messages = imap.select("INBOX")
        messages = int(messages[0])

        break_flag = False
        result = []
        while(break_flag != True):
            # fetch the email message by ID
            new_string = ""
            if (keywords == []):
                keyword_flag = True
            else:
                keyword_flag = False
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
                    email_date = msg['Date']
                    email_date_object = create_email_datetime(email_date)
                    if (email_date_object < previous_query_time):
                        break_flag = True
                        break
                    new_string += ("Date: " + email_date_object.strftime("%Y-%m-%d %H:%M") + " SGT\n")
                    new_string += ("Subject: " + subject + "\n")
                    new_string += ("From: " + From + "\n")

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
                                new_string += (body + "\n")
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            new_string += (body + "\n")
            for i in keywords:
                if(i.upper() in new_string.upper()):
                    keyword_flag = True
                    break
            if((break_flag != True) and (keyword_flag == True)):
                result.append(new_string)
            messages -= 1
            if (messages == 0):
                break_flag = True
                break
        # close the connection and logout
        imap.close()
        imap.logout()
        return result

print(scrape("whatever93201@mail.com", "A!@345678!", 6, datetime.now() - timedelta(hours=6), []))

# whatever1239042@outlook.com
# A!@345678

# whatever93201@mail.com
# A!@345678!