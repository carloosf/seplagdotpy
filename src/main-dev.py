import json
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from message import MSG

load_dotenv()

SERVER = os.getenv('SERVER')
PW = os.getenv('PASSWORD')
REMETENTE = os.getenv('REMETENTE')
DESTINATARIOS = json.loads(os.environ['DESTINATARIOS'])
PORTA = os.getenv('PORTA')


def send_mail(assunto):
    msg = MIMEMultipart('related')
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = assunto

    part = MIMEText(MSG, 'html')
    msg.attach(part)

    image_path = './static/banner-solo.png'
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='header.png')
        image.add_header('Content-ID', '<header_img>')
        msg.attach(image)

    # Send the email
    with smtplib.SMTP(SERVER, PORTA) as server:
        server.starttls()
        server.login(REMETENTE, PW)
        server.sendmail(REMETENTE, DESTINATARIOS, msg.as_string())


if __name__ == '__main__':
    send_mail('Grupo de Python da SEPLAG')
