class Mail:
    Subject = ''
    To = []
    From = ''
    Date = ''
    Content = ''
    attachments = []
    Type = 'plain' # or 'html'
    charset = 'utf-8'
    uid = ''
    # for send html mail
    htmlPath = ''
    # store mail message
    message = None

    def __str__(self) -> str:
        result = """
From: {0.From!s}
Subject: {0.Subject!s}
To: {0.To!s}
Date: {0.Date!s}
Attachments: {0.attachments!s}
Content: 
{0.Content!s}
        """.format(self)
        return result

