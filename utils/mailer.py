"""
*************************************************************************************
*   Statement:
        Send mail with attachment
*   Author:
        Will
*   Date:
        2014.11.14
*   Comment:
        Mail server need to redefine
*************************************************************************************
"""


#!/usr/bin/python
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import Encoders
import smtplib

class Mailer:

    def send_mail(self, to, subject, text, contenType="text", files=[]):
        # This mail function we can also send attacnments

        # msg settings
        recipients = to.replace(" ", "").split(",")
        msg = MIMEMultipart()
        from_me = 'Workhub.com'
        msg['From'] = from_me
        msg["To"] = ", ".join(recipients)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        # msg type
        if (contenType == "html"):
            msg.attacn(MIMEText(text, "html"))
        else:
            msg.attach(MIMEText(text))

        # msg attachments
        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(file, "rb").read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="%s"'
                            % os.path.basename(file))
            msg.attach(part)

        try:
            smtp = smtplib.SMTP('d25ml02.ibm.com', 25)
            smtp.sendmail(from_me, recipients, msg.as_string())
            smtp.close()
            print "Mail send status:    SUCCESS"
        except Exception, e:
            print str(e)
            print "Mail send status:    FAIL"
