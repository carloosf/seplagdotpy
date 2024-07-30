# database.py
import psycopg2
from psycopg2 import sql
from typing import List, Tuple
from datetime import datetime

class Database:
    def __init__(self, host: str, database: str, user: str, password: str, port: int):
        self.db_config = {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'port': port
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.db_config)
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
            query = sql.SQL("""
                SELECT * FROM {} WHERE "date" = %s
            """).format(sql.Identifier(table_name))
            
            self.cursor.execute(query, (date,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar registros: {e}")
            return []
        
    def fetch_records_user(self, table_name: str) -> List[Tuple]:
        if not self.conn:
            raise ConnectionError("Não há conexão com o banco de dados.")
        try:
            query = sql.SQL("""
                SELECT * FROM {}
            """).format(sql.Identifier(table_name))
            
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar registros: {e}")
            return []
