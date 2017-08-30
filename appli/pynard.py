#!/usr/bin/env python

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
@app.route('/home/')
def index():
    title="Welcome in pynard, your cave manager"
    page_title = "Pynard"
    options_label = ["Add bottles","Remove bottles","Display the stock","Display the bottles which nee to be drink"]
    return render_template('index.html', options_label = options_label, title = title, page_title = page_title)    












#    elif action == "2":
#        print "remove bottle(s) from the stock"













