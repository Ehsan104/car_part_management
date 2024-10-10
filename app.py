from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)

#first lets initlize the database 
db = TinyDB('car_parts.json') #This will create a json file called car_parts.json (this will be considered the database)

@app.route('/')
def index():
    parts = db.all() #This will get all the parts in the database
    return render_template('index.html', parts=parts)`

#This is where the all the functions will be defined

@app.route('/add', methods=['POST'])
def add_part(): 
    #this function will add a part to the database

@app.route('/delete', methods=['POST'])
def delete_part():
    #this function will delete a part from the database

@app.route('/lookup', methods=['POST'])
def lookup_part():
    #this function will look up a part in the database

@
