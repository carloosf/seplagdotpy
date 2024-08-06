import os
import smtplib
from typing import List, Tuple
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

class DataHandler:
    def __init__(self, schedule_data: List[Tuple], user_data: List[Tuple], db):
        self.schedule_data = schedule_data
        self.user_data = user_data
        self.db = db
        load_dotenv()

    def send_emails(self):
        if not self.schedule_data or not self.user_data:
            print("Nenhum dado disponível.")
            return

        SERVER = os.getenv('SERVER')
        PW = os.getenv('PASSWORD')
        REMETENTE = os.getenv('REMETENTE')
        PORTA = int(os.getenv('PORTA'))

        for record in self.schedule_data:
            record_id = record[0]
            html_content = record[1]
            html_content = html_content.replace("logo.png", "cid:banner.png")

            for user in self.user_data:
                user_email = user[1]

                msg = MIMEMultipart('related')
                msg['From'] = REMETENTE
                msg['To'] = user_email
                msg['Subject'] = 'Newsletter da SEPLAG'

                part = MIMEText(html_content, 'html', 'utf-8')
                msg.attach(part)

                image_path = './static/banner.png'
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as image_file:
                        image = MIMEImage(image_file.read(), name='banner.png')
                        image.add_header('Content-ID', '<banner.png>')
                        msg.attach(image)

                try:
                    with smtplib.SMTP(SERVER, PORTA) as server:
                        server.starttls()
                        server.login(REMETENTE, PW)
                        server.sendmail(REMETENTE, user_email, msg.as_string())
                        print(f"Email enviado para {user_email}")
                        self.db.update_send_status('Agendamento', record_id, True)
                except Exception as e:
                    print(f"Erro ao enviar email para {user_email}: {e}")

    def display_records(self):
        if not self.schedule_data:
            print("Nenhum dado disponível.")
            return

        for record in self.schedule_data:
            html_content = record[3]
            print(html_content)
