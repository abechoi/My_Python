# Mailing Client

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# smtp.STMP( server, port number )
# server = smtplib.SMTP("mail.yahoo.com", 25)
server = smtplib.SMTP("smtp.gmail.com", 25)
server.connect("smtp.gmail.com", 465)

server.ehlo()

# r = reading type
with open("password.txt", "r") as f:
  password = f.read()

server.login("choi209@mail.chapman.edu", password)

msg = MIMEMultipart()
msg["From"] = "PythonTest"
msg["To"] = "Abe Choi"
msg["Subject"] = "This is a test email"

# r = reading type
with open("message.txt", "r") as f:
  message = f.read()

# MIMEMultipart().attach( message, text type )
msg.attach(MIMEText(message, "plain"))

filename = "Kayak1-small.jpg"
# rb = reading-byte type
attachment = open(filename, "rb")

# create payload
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f'attachment; filename={filename}')
# attach the payload to the message
msg.attach(p)

text = msg.as_string()

server.sendmail("choi209@mail.chapman.edu", "abraham.choi@rocketmail.com", text)
server.quit()