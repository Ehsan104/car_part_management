from flask import Flask 
import sqlite3

app = Flask(__name__)

#first lets initlize the database 
def database():
    conn = sqlite3.connect('parts.db')
    c = conn.cursor()
    conn.execute('CREATE TABLE parts (part_name TEXT, part_category TEXT, part_price TEXT, part_quantity TEXT, part_manufacturer TEXT)')
    conn.commit()
    conn.close()
database()

@app.route('/')
    def index():
        conn = sqlite3.connect('parts.db')
        c = conn.cursor()
        c.execute('SELECT * FROM parts')
        parts = c.fetchall()
        conn.close()
        return render_template('index.html', parts=parts)

#This is where the all the functions will be defined

@app.route('/add', methods=['POST'])
def add_part():
    part_name = request.form['part_name']
    part_category = request.form['part_category']
    part_price = request.form['part_price']
    part_quantity = request.form['part_quantity']
    part_manufacturer = request.form['part_manufacturer']
    
      



@app.route('/delete', methods=['POST'])
