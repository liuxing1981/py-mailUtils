# mailUtils Description
Easy for search mail by sender,date,subject,mail content, and download attachments.
Easy for send plain mail,html mail,and attachments

## How to use
#### clone the project
```bash
git clone 
cd mailUtils
python setup.py install
```

## example
### QQ mail server need to send open imap
* login to mail.qq.com
* 设置-账户-POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务
* 开启IMAP(需要手机发个短信)
### receive mail
```bash
from mailUtils import *

if __name__=='__main__':
    username = 'yourname@qq.com'
    password = ''
    with ImapClient('imap.qq.com:993',username, password，attachment_save_path='e:\\') as client:
        # default select folder is INBOX
        client.select_folders()
        criteria = Criteria()
        # find mails by sender rual or ziden
        query1 = criteria.findBySenders('rual','ziden@worldcup.com')
        # find mails by date from 2019-12-17 to now
        query2 = criteria.findByDateFrom('2019-12-17')
        # find mails on date 2019-12-17
        query3 = criteria.findByDate('2019-12-17')
        # find mails by mail content
        query4 = criteria.findByContent('hello world')
        
        # combine the criteria 
        criteria.and_(query1)
        criteria.and_(query2)
        # execute query and return a list
        mails = client.executeQuery(criteria)
        # mails = client.queryByUid('448')
        for mail in mails:
            print(mail)
```

### send mail
```bash
from mailUtils import *
username = ''
password = ''
client = SendMail(QQServer.SMTP,username, password)
# build a mail
mail = Mail()
mail.From = 'your@qq.com'
mail.To = mail.From
mail.Subject = 'Test mail'

# send text mail
mail.Content = '''
Hello world
This is a test mail
'''

# send html mail
mail.htmlPath = 'e:\\report.html'

# with attachments
mail.attachments = ['e:\\hss.schema.modify.ldif']
# send mail
client.send_mail(mail)
```
