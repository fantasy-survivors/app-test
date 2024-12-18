from utils import connect_database

def insert_data():
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO team (id, name) VALUES (1, 'John'), (2, 'Tom'), (3, 'Curry');")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    insert_data()
    print("Data inserted successfully")
