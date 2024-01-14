
from db import *
from datetime import *
import time
import sys
import mysql.connector
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True
cnx = mysql.connector.connect(user='remoteAccess', password='1234abcz',host='35.189.78.49', port=3306)
cursor = cnx.cursor()
create_database(cnx,cursor)

@app.route('/', methods=['GET', 'POST'])
def login():
     error = None
     if request.method == 'POST':
          username= request.form['username']
          password= request.form['password']
          
          cnx = mysql.connector.connect(user='remoteAccess', password='1234abcz',host='35.189.78.49', port=3306)
          cursor = cnx.cursor(buffered=True)
          if check_if_user_exists(cnx,cursor,username,password):
               return redirect("http://35.242.152.88/username=%s" % username)
          else:
               error = "Wrong password or username"
     return render_template('login.html', error=error)

@app.route('/Sub')
def sub_page():
    return 'Sub Page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
         username= request.form['username']
         password= request.form['password']
         
         cnx = mysql.connector.connect(user='remoteAccess', password='1234abcz',host='35.189.78.49', port=3306)
         cursor = cnx.cursor()
         insert_user(cnx,cursor,username,password)
         
         return redirect(url_for('login'))
    return render_template('register.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="8080")
