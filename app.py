from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/project_form')
def project_form():
    return render_template('project.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        age = request.form['age']
        flight_distance = request.form['flight_distance']
        inflight_entertainment = request.form['inflight_entertainment']
        baggage_handling = request.form['baggage_handling']
        cleanliness = request.form['cleanliness']
        departure_delay = request.form['departure_delay']
        arrival_delay = request.form['arrival_delay']
        gender = request.form['gender']
        customer_type = request.form['customer_type']
        class_ = request.form['Class']
        type_of_travel = request.form['type_of_travel']

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO customer_satisfaction (
                age, flight_distance, inflight_entertainment,baggage_handling, cleanliness, departure_delay,arrival_delay, gender, customer_type, class, type_of_travel) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (age, flight_distance, inflight_entertainment,baggage_handling, cleanliness, departure_delay,arrival_delay, gender, customer_type, class_,type_of_travel))

        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
