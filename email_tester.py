import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Captured Image'
    msg['From'] = "testersender2002@gmail.com"
    msg['To'] = "testerreciever2002@gmail.com"

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('testersender2002@gmail.com', 'Pravin@123')
    s.sendmail('testersender2002@gmail.com', 'testerreciever2002@gmail.com', msg.as_string())
    s.quit()
