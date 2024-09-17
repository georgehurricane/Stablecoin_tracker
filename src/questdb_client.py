# src/questdb_client.py

import requests
from src.config import QUESTDB_URL

class QuestDBClient:
    def __init__(self):
        self.url = QUESTDB_URL

    def insert_data(self, table_name, data):
        # Prepare the SQL insert statement
        sql = f"INSERT INTO {table_name} VALUES "
        sql += ', '.join([f"('{item['address']}', '{item['transaction_hash']}', '{item['value']}', '{item['timestamp']}')" for item in data])
        response = requests.post(f"{self.url}/insert", data=sql)
        return response.status_code == 200
