from mailUtils import SendMail, Mail

client = SendMail('mailrelay.int.nokia.com:25')

def send_html():
    mail = Mail()
    mail.From = 'rex@qq.com'
    mail.To = 'xing.1.liu@nokia-sbell.com'
    mail.Subject = 'Html only'
    mail.htmlPath = 'e:\\report.html'
    mail.Type = 'html'
    client.send_mail(mail)

def send_html_attach():
    mail = Mail()
    mail.From = 'xing.1.liu@nokia-sbell.com'
    mail.To = 'xing.1.liu@nokia-sbell.com'
    mail.Subject = 'Html with attach'
    mail.htmlPath = 'e:\\report.html'
    mail.Type = 'html'
    mail.attachments = ['e:\\bug2.PNG']
    client.send_mail(mail)

def send_text():
    mail = Mail()
    mail.From = 'rex@qq.com'
    mail.To = 'xing.1.liu@nokia-sbell.com'
    mail.Subject = 'Text with attach'
    mail.Content = 'Hello world\n BR Luis'
    # mail.attachments = ['e:\\report.html']
    client.send_mail(mail)

# send_text()
# send_html()
send_html_attach()