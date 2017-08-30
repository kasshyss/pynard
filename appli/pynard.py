#!/usr/bin/env python

from flask import Flask, render_template


app = Flask(__name__)


#Application start point
@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
@app.route('/home/')
def index():
    title="Welcome in pynard, your cave manager"
    page_title = "Pynard"
    options_label = ["Add bottles","Remove bottles","Display the stock","Display the bottles which nee to be drink"]
    return render_template('index.html', options_label = options_label, title = title, page_title = page_title)    


#Application add bottle point
@app.route('/add')
def add_bottle():
    title="Add new bootles to your cave"
    page_title = "Pynard"
    return render_template('add.html', title = title, page_title = page_title)    

