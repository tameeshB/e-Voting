import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from polls.globals import globals

def dictGet(hashMap, key):
    try:
        return hashMap[key]
    except KeyError:
        return ""
def sendMail(to, subject, body):
    print(to, subject, body)
    if not to or not subject or not body:
        return False
    try:
        s = smtplib.SMTP(
            host = os.environ.get('smtp_host') or globals['smtp']['host'],
            port = os.environ.get('smtp_host') or globals['smtp']['host']
        )
        s.starttls()
        s.login(
            os.environ.get('smtp_sender') or globals['smtp']['sender'], 
            os.environ.get('smtp_pass') or globals['smtp']['pass']
        )
        msg = MIMEMultipart()
        msg['From']=os.environ.get('smtp_sender') or globals['smtp']['sender']
        msg['To']=to
        msg['Subject']=subject
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return True
    except:
        return False