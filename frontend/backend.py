import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from datetime import datetime, timedelta

previous_query_time = datetime.now() - timedelta(hours = 1)
# print(previous_query_time)

# Create Datetime from Email_date
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

email_dict = {
    "gmail" : "imap.gmail.com",
    "outlook" : "imap-mail.outlook.com",
    "yahoo" : "imap.mail.yahoo.com",
    "office_365" : "outlook.office365.com",
    "yahoo_plus" : "plus.imap.mail.yahoo.com",
    "mail_com" : "imap.mail.com"
}

# Sort email by email provider
def email_sort(email_address):
    if("@gmail" in email_address):
        return "gmail"
    elif("@outlook" in email_address or "@u.nus.edu" in email_address or "@hotmail" in email_address):
        return "outlook"
    elif("@yahoo" in email_address):
        return "yahoo"
    else:
        return "mail_com"

# Authenticate email_address and password
def authenticate(email_address, password):
    try:
        imap = imaplib.IMAP4_SSL(email_dict[email_sort(email_address)])
        imap.login(email_address, password)
    except:
        return False
    else:
        return True

# Scrape user_inbox for relevant emails that match keywords
def scrape(email_address, password, frequency, last_query, keywords):
    previous_query_time = datetime.now()
    if (datetime.now() - last_query < timedelta(hours = frequency)):
        previous_query_time = last_query
    else:
        previous_query_time = (datetime.now() - timedelta(hours = frequency))
    # print(previous_query_time)
    try:
        imap = imaplib.IMAP4_SSL(email_dict[email_sort(email_address)])
        imap.login(email_address, password)
    except:
        return 'authentication failed'
    else:
        status, messages = imap.select("INBOX")
        messages = int(messages[0])

        break_flag = False
        result = ["The following emails are from " + email_address + "'s inbox."]
        result.append("="*25)
        while(break_flag != True):
            # Fetch the email message matching the message ID
            new_string = ""
            if (keywords == []):
                keyword_flag = True
            else:
                keyword_flag = False
            res, msg = imap.fetch(str(messages), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # Recover an email message from bytes object
                    msg = email.message_from_bytes(response[1])
                    # Decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # Further decode to string if subject is a bytes object
                        subject = subject.decode(encoding)
                    # Decode the address of email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        # Further decode to string if From is a bytes object
                        From = From.decode(encoding)
                    email_date = msg['Date']
                    email_date_object = create_email_datetime(email_date)
                    if (email_date_object < previous_query_time):
                        # Break from loop as current email was received before previous_query_time
                        break_flag = True
                        break
                    # Concatenate string with information from email
                    new_string += ("Date: " + email_date_object.strftime("%Y-%m-%d %H:%M") + " SGT\n")
                    new_string += ("Subject: " + subject + "\n")
                    new_string += ("From: " + From + "\n")

                    # If the email body is a multipart message
                    if msg.is_multipart():
                        # Iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # Obtain email body message
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
                if(str(i).upper() in str(new_string).upper()):
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
        result.append("="*25)
        return result

# print(authenticate("noreplytest2468@gmail.com", "A12345678!"))

print(scrape("whatever12093@gmail.com", "A12345678!", 6, datetime.now() - timedelta(hours=6), ["sand"]))

# whatever1239042@outlook.com
# A!@345678

# whatever93201@mail.com
# A!@345678!

## not working
#noreplytest2468@gmail.com
#A12345678!