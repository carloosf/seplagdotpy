from database import Database
from data_handler import DataHandler
from datetime import datetime

def main():
    db_config = {
        'database': '../seplag.py/server/prisma/dev.db'
    }

    db = Database(**db_config)
    db.connect()
    
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        schedule_records = db.fetch_records_by_date('Agendamento', today)
        user_records = db.fetch_records_user('User')

        data_handler = DataHandler(schedule_records, user_records, db)
        data_handler.send_emails()
    
    finally:
        db.disconnect()

if __name__ == "__main__":
    main()
