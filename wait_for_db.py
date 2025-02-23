import os
import time
import psycopg2

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv('POSTGRES_DB', 'neirochef'),
                user=os.getenv('POSTGRES_USER', 'postgres'),
                password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
                host=os.getenv('POSTGRES_HOST', 'db'),
                port=os.getenv('POSTGRES_PORT', '5432')
            )
            conn.close()
            break
        except psycopg2.OperationalError:
            print('Waiting for database...')
            time.sleep(1)

if __name__ == '__main__':
    wait_for_db() 