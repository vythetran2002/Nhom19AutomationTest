import imaplib
import email
from email.header import decode_header

class GetOTP():

    def getOTP(self):

        # login to the Gmail account
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        username = "20110752@student.hcmute.edu.vn"
        password = "okbabylady="
        imap.login(username, password)

        # select the mailbox and search for the latest message
        imap.select("inbox")
        status, messages = imap.search(None, "ALL")
        message_ids = messages[0].split(b' ')

        # fetch the newest message
        status, message = imap.fetch(message_ids[-1], "(RFC822)")

        # parse the message
        raw_message = message[0][1]
        email_message = email.message_from_bytes(raw_message)

        # extract the message details
        subject = decode_header(email_message["Subject"])[0][0]
        from_ = decode_header(email_message["From"])[0][0]
        to = decode_header(email_message["To"])[0][0]
        body = ""

        # extract the message body
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body += part.get_payload(decode=True).decode()
        else:
            body = email_message.get_payload(decode=True).decode()

        #close the mailbox and logout from the account
        imap.close()
        imap.logout()

        # print the message details and body

        start_string= '0;">'
        end_string = "</span"

        # find the start and end index of the substring
        start_index = body.find(start_string)
        end_index = body.find(end_string)

        # extract the substring
        substring = body[start_index:end_index+1]

        start_index2 = substring.find('>')
        end_index2 = substring.find('<')

        otp = substring[start_index2 + 1: end_index2]

        return otp

    def getReturnedPasswd(self):
        # login to the Gmail account
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        username = "20110752@student.hcmute.edu.vn"
        password = "okbabylady="
        imap.login(username, password)

        # select the mailbox and search for the latest message
        imap.select("inbox")
        status, messages = imap.search(None, "ALL")
        message_ids = messages[0].split(b' ')

        # fetch the newest message
        status, message = imap.fetch(message_ids[-1], "(RFC822)")

        # parse the message
        raw_message = message[0][1]
        email_message = email.message_from_bytes(raw_message)

        # extract the message details
        subject = decode_header(email_message["Subject"])[0][0]
        from_ = decode_header(email_message["From"])[0][0]
        to = decode_header(email_message["To"])[0][0]
        body = ""

        # extract the message body
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body += part.get_payload(decode=True).decode()
        else:
            body = email_message.get_payload(decode=True).decode()

        # close the mailbox and logout from the account
        imap.close()
        imap.logout()

        start_string = '0;">'
        end_string = "</span"

        # find the start and end index of the substring
        start_index = body.find(start_string)
        end_index = body.find(end_string)

        # extract the substring
        substring = body[start_index:end_index + 1]

        start_index2 = substring.find('>')
        end_index2 = substring.find('<')

        newPasswd = substring[start_index2 + 1: end_index2]

        return newPasswd
