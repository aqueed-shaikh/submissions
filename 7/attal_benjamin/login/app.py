#!/usr/local/bin/python
from flask import Flask, session, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  if 'username' in session:
    return render_template('index.html')
  redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #Authenitcation with database
    return redirect(url_for('home'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('home'))

@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    #Add to database
  return render_template('register.html')
  

if __name__ = '__main__'
  app.run(debug=True,host='0.0.0.0',port=5000)
