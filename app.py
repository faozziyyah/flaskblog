from turtle import title
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime, json, psycopg2

app = Flask(__name__)

app.secret_key = 'secret'
def get_db_connection():
  #conn = psycopg2.connect("dbname=todolist user=postgres password=opeyemi2001 host=localhost")
  conn = psycopg2.connect("postgres://bavagbbtdgtzoa:2439f75b5f04f05796edebfc652f6a95eb52069d2be8f6435d992525429e9ecc@ec2-3-213-66-35.compute-1.amazonaws.com:5432/d6741jm75u6uh6")
  return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from todos')
    rv = cur.fetchall()
    for item in rv:
        print(item)
    cur.close()
    return render_template('index.html', todos=rv)

@app.route('/add', methods=['POST'])
def add():
    if request.method == "POST":
        id = request.form['id']
        title = request.form['title']

        if id and title:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('insert into todos(id, title, completed) VALUES (%s, %s, %s)', (id, title, False))
            conn.commit()
            cur.close()
        else:
            flash('Please fill all fields', 'flash_error')  
            return redirect(url_for('index'))      
        flash('todo successfully added!')

    return redirect(url_for('index'))

@app.route('/update/<string:id>', methods =['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('update todos set completed = True where id=%s', (id))
    conn.commit()
    #rv = cur.fetchall()
    #student = rv
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete(id):
    flash('student record deleted successfully')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(' delete from todos where id=%s', (id))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)