import sqlite3

def create_table():
    conn = sqlite3.connect('database.db') 
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_satisfaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER NOT NULL,
    flight_distance INTEGER NOT NULL,
    inflight_entertainment INTEGER NOT NULL,
    baggage_handling INTEGER NOT NULL,
    cleanliness INTEGER NOT NULL,
    departure_delay INTEGER NOT NULL,
    arrival_delay INTEGER NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female')) NOT NULL,
    customer_type TEXT CHECK(customer_type IN ('Loyal Customer', 'Disloyal Customer')) NOT NULL,
    class TEXT CHECK(class IN ('Eco Plus', 'Business', 'Eco')) NOT NULL,
    type_of_travel TEXT CHECK(type_of_travel IN ('Personal Travel', 'Business Travel')) NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
