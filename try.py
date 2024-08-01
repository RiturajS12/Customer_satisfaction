import sqlite3

def check_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Print the table schema
    cursor.execute("PRAGMA table_info(customer_satisfaction)")
    schema = cursor.fetchall()
    print("Table Schema:")
    for row in schema:
        print(row)

    # Print the table contents
    cursor.execute("SELECT * FROM customer_satisfaction")
    rows = cursor.fetchall()
    print("\nTable Data:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == '__main__':
    check_db()
