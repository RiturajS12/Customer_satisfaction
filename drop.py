import sqlite3

def drop_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS customer_satisfaction")
    conn.commit()

    print("Table dropped successfully.")

    conn.close()

if __name__ == '__main__':
    drop_table()
