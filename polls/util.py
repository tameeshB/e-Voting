import smtplib,os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from polls.globals import globals

def dictGet(hashMap, key):
    try:
        return hashMap[key]
    except KeyError:
        return ""
def sendMail(to, subject, body, html=""):
    print(to, subject, body)
    if not to or not subject or not body:
        return False
    try:
        s = smtplib.SMTP(
            host = os.environ.get('smtp_host') or globals['smtp']['host'],
            port = os.environ.get('smtp_port') or globals['smtp']['port']
        )
        s.starttls()
        s.login(
            os.environ.get('smtp_sender') or globals['smtp']['sender'], 
            os.environ.get('smtp_pass') or globals['smtp']['pass']
        )
        msg = MIMEMultipart('alternative')
        msg['From']=os.environ.get('smtp_sender') or globals['smtp']['sender']
        msg['To']=to
        msg['Subject']=subject
        plainTextBody = MIMEText(body, 'plain')
        msg.attach(plainTextBody)
        if html:
            htmlBody = MIMEText(html, 'html')
            msg.attach(htmlBody)
        s.send_message(msg)
        # s.sendmail(msg['From'], msg['To'], msg.as_string())
        return True
    except:
        return False