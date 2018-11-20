import smtplib,os,csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from polls.globals import globals
from polls.models import ConfigVars

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

def initConfigTable():
    nConfigVars = len(ConfigVars.objects.filter())
    if nConfigVars < 2:
        ConfigVars.objects.all().delete()
        ongoing = ConfigVars(varKey='ongoing')
        ongoing.save()
        publish = ConfigVars(varKey='publish')
        publish.save()

def parsePdf(filepath, roll_col, webmail_col):
    result = {'status': False,'data': "Error"}

    try:
        import tabula
    except ModuleNotFoundError:
        result['status'] = False
        result['data'] = "Dependency tabula not found! Please upload .csv instead"
        return result

    df = tabula.read_pdf(filepath, options="--pages all", pandas_options={'header': None})

    if not (0 <= roll_col < len(df.columns)):
        result['status'] = False
        result['data'] = "Invalid Roll no. column - not in range 0 to %d" % (len(df.columns)-1)
        return result

    if not (0 <= webmail_col < len(df.columns)):
        result['status'] = False
        result['data'] = "Invalid Webmail column - not in range 0 to %d" % (len(df.columns)-1)
        return result

    roll_no_li = list(df[df.columns[roll_col]])
    webmail_li = list(df[df.columns[webmail_col]])

    result['status'] = True
    result['data'] = [roll_no_li , webmail_li]
    return result

def parseCsv(filepath, roll_col, webmail_col):
    result = {'status': False,'data': "Error"}

    with open(filepath, 'r') as f:
        csv_reader = csv.reader(f)
        num_columns = len(next(csv_reader))

    if not (0 <= roll_col < num_columns):
        result['status'] = False
        result['data'] = "Invalid Roll no. column - not in range 0 to %d" % (num_columns-1)
        return result

    if not (0 <= webmail_col < num_columns):
        result['status'] = False
        result['data'] = "Invalid Webmail column - not in range 0 to %d" % (num_columns-1)
        return result

    with open(filepath, 'r') as f:
        csv_reader = csv.reader(f)
        roll_no_li = []
        webmail_li = []
        for line in csv_reader:
            roll_no_li.append(line[roll_col])
            webmail_li.append(line[webmail_col])

    result['status'] = True
    result['data'] = [roll_no_li , webmail_li]
    return result

def parseEmailIds(filepath, roll_col, webmail_col):
    print ("::",filepath,"::")
    try:
        roll_col = int(roll_col)
    except ValueError:
        return {'status': False, 'data': "Invalid Roll no. column"}
    try:
        webmail_col = int(webmail_col)
    except ValueError:
        return {'status': False, 'data': "Invalid Webmail column"}

    if filepath.endswith(".pdf"):
        result = parsePdf(filepath, roll_col, webmail_col)
    elif filepath.endswith(".csv"):
        result = parseCsv(filepath, roll_col, webmail_col)
    else:
        result = {'status': False, 'data': 'Unknown file format! Please upload .csv or .pdf'}

    return result
