import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email = "your email"
password = "your password"

def send_email():
    msg = MIMEMultipart()
    msg['subject'] = 'Webcam Alert!'

    body = "There are someone trying to use your laptop!"
    msg.attach(MIMEText(body, 'plain'))

    filename = 'saved_img.jpg'
    attachment =open(filename, 'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.office365.com', 587) #if gmail, change to smtp.gmail.com
    server.starttls()
    server.login(email, password)

    server.sendmail(email, email, text)
    server.quit()
