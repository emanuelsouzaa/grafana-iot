import psycopg2
from psycopg2 import OperationalError
import time
import random
from os import getenv
from datetime import datetime

def wait_for_db():
    for i in range(10):
        try:
            conn = psycopg2.connect(
                dbname=getenv('DATABASE_NAME'),
                user=getenv('DATABASE_USER'),
                password=getenv('DATABASE_PASSWORD'),
                host='postgres',
                port='5432'
                )
            
            print("Conexão com PostgreSQL bem-sucedida!")
            return conn
        except OperationalError:
            print(f"Tentativa {i+1}/10: PostgreSQL ainda não está pronto. Esperando 3s...")
            time.sleep(3)
    raise Exception("Não foi possível conectar ao banco após várias tentativas.")


conn = wait_for_db()
curr = conn.cursor()


sensors = [
    {
        "id": 1, "unit": "C"
    },
    {
        "id": 2, "unit": "C"
    },
    {
        "id": 3, "unit": "C"
    },
    {
        "id": 4, "unit": "C"
    },
]


def get_value():
    return round(random.uniform(20.0, 36.0), 2)


try:
    while True:
        for sensor in sensors:
            value = get_value()
            date = datetime.now().isoformat(sep=' ', timespec="seconds")
            curr.execute(
                """
                INSERT INTO data_sensors (id, date, value, unit)
                VALUES (%s, %s, %s, %s)
                """
            , (
                sensor['id'],
                date,
                value,
                sensor['unit']
            ))
            
            print(f"Sensor id {sensor['id']}: {value} °C")
            
        conn.commit()
        time.sleep(3 * 60)
        
except KeyboardInterrupt:
    print('Closing...')
    curr.close()
    conn.close()