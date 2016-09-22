import sqlite3
import time
conn = sqlite3.connect('logTime.db')
c = conn.cursor()
def insert_date():
    d = time.strftime("%Y-%m-%d")
    return d

def insert_time():
    t = time.strftime("%H-%M-%S")
    return t

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS logTime(date TEXT, time TEXT)')
def insert():
    c.execute("INSERT INTO logTime VALUES (?, ?);", (insert_date(), insert_time()))
    conn.commit()

    c.close
    print("all finished...")
    conn.close()

def main():
    create_table()
    insert()
    print("done")

main()
