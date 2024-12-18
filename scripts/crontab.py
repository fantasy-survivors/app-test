from utils import connect_database

def main():
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM team;")
    data = cur.fetchone()
    print(data)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()