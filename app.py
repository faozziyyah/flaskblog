from turtle import title
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime, json, psycopg2

app = Flask(__name__)

app.secret_key = 'secret'
def get_db_connection():
  conn = psycopg2.connect("dbname=todolist user=postgres password=opeyemi2001 host=localhost")
  #conn = psycopg2.connect("postgres://lrqtcehzeiejyl:48466d99f2102da9054a975354b4322becfede3381f3777ffcc0a649d7c54009@ec2-35-168-122-84.compute-1.amazonaws.com:5432/dbfh4rod9jc9tg")
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