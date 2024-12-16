import psycopg2
import os

def create_table():
    """
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100)
    );
    """

def insert_data():
    host = os.getenv('POSTGRES_HOST', "192.168.0.155")
    port = os.getenv('POSTGRES_PORT', '5432')
    user = os.getenv('POSTGRES_USER', 'myuser')
    password = os.getenv('POSTGRES_PASSWORD', 'mypassword')
    dbname = os.getenv('POSTGRES_DB', 'mydb')

    print(f"host: {host}")
    print(f"port: {port}")
    print(f"user: {user}")
    print(f"password: {password}")
    print(f"dbname: {dbname}")
    conn = psycopg2.connect(
        host=host,
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO team (id, name) VALUES (1, 'John'), (2, 'Tom'), (3, 'Curry');")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    insert_data()
    print("Data inserted successfully")
