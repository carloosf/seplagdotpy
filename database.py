import sqlite3
from typing import List, Tuple
from sqlite3 import Connection, Cursor


class Database:
    def __init__(self, database: str):
        self.db_config = {
            'database': database
        }
        self.conn: Connection = None
        self.cursor: Cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_config['database'])
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def disconnect(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def fetch_records_by_date(self, table_name: str, date: str) -> List[Tuple]:
        if not self.conn:
            raise ConnectionError("Não há conexão com o banco de dados.")

        try:
            query = f"""
                SELECT * FROM {table_name} WHERE date = ? AND send = 0
            """
            self.cursor.execute(query, (date,))
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Erro ao buscar registros: {e}")
            return []

    def fetch_records_user(self, table_name: str) -> List[Tuple]:
        if not self.conn:
            raise ConnectionError("Não há conexão com o banco de dados.")
        try:
            query = f"""
                SELECT * FROM {table_name}
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar registros: {e}")
            return []

    def update_send_status(self, table_name: str, record_id: int, status: bool):
        if not self.conn:
            raise ConnectionError("Não há conexão com o banco de dados.")
        try:
            query = f"""
                UPDATE {table_name} SET "send" = ? WHERE "id" = ?
            """
            self.cursor.execute(query, (1 if status else 0, record_id))
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar status de envio: {e}")
            self.conn.rollback()
