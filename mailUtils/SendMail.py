import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from idna import unicode

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

class SendMail():
    def __init__(self, socket, username='', password=''):
        self.server,self.port = socket.split(':')
        self.port = int(self.port)
        self.username = username
        self.password = password

    def createMessage(self,mail):
        message = MIMEMultipart()
        message['From'] = _format_addr('<%s>' % mail.From)
        message['To'] = _format_addr('<%s>' % mail.To)
        message['Subject'] = Header(mail.Subject, mail.charset)
        if mail.Type == 'html':
            with open(mail.htmlPath, 'rt', encoding=mail.charset) as fp:
                mail.Content = fp.read()
        message.attach(MIMEText(mail.Content, mail.Type, mail.charset))
        for path in mail.attachments:
            att = MIMEText(open(path, 'rb').read(), 'base64', mail.charset)
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"'%os.path.basename(path)
            message.attach(att)
        return message

    # def _textMail(self,mail):
    #     message = MIMEText(mail.Content, mail.Type, mail.charset)
    #     message['From'] = _format_addr('<%s>'%mail.From)
    #     message['To'] = _format_addr('<%s>'%mail.To)
    #     message['Subject'] = Header(mail.Subject, mail.charset)
    #     return message
    #
    # def _htmlMail(self, mail):
    #     with open(mail.htmlPath, 'rt', encoding=mail.charset) as fp:
    #         mail.Content = fp.read()
    #     message = MIMEText(mail.Content, mail.Type, mail.charset)
    #     message['From'] = _format_addr('<%s>' % mail.From)
    #     message['To'] = _format_addr('<%s>' % mail.To)
    #     message['Subject'] = Header(mail.Subject, mail.charset)
    #     return message

    def send_mail(self, mail):
        message = self.createMessage(mail)
        try:
            smtpObj = None
            if self.port == smtplib.SMTP_PORT:
                smtpObj = smtplib.SMTP(self.server,self.port)
            elif self.port == smtplib.SMTP_SSL_PORT:
                smtpObj = smtplib.SMTP_SSL(self.server,self.port)
            # smtpObj.set_debuglevel(1)
            # smtpObj.ehlo()
            # smtpObj.starttls()
            # smtpObj.ehlo
            if self.username != '' and self.password != '':
                smtpObj.login(self.username, self.password)
            smtpObj.sendmail(mail.From, mail.To.split(','), message.as_string())
            print("send successfully!")
            smtpObj.close()
        except smtplib.SMTPException as e:
            print("Error: mail send failed!")
            print(e)