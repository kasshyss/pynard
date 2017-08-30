#!/usr/bin/env python

from flask import Flask, render_template, request


app = Flask(__name__)


#Application start point
@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
@app.route('/home/')
def index():

    title="Welcome in pynard, your cave manager"
    page_title = "Pynard"
    options_label = [["Add bottles", "add"],["Remove bottles", "remove"],["Display the stock", "stock"],["Display the bottles which nee to be drink", "to_drink"]]
    return render_template('index.html', options_label = options_label, title = title, page_title = page_title)

#Application add bottle point
@app.route('/add/')
def add_bottle():
    title="Add new bootles to your cave"
    page_title = "Pynard"
    return render_template('add.html', title = title, page_title = page_title)    

#Application remove from the stock
@app.route('/remove/')
def rm_bottle():
    page_title = "Pynard"
    title="Remove bootles to your cave"
    return render_template('remove.html', title = title, page_title = page_title)    

#Display the stock
@app.route('/stock/')
def stock():
    page_title = "Pynard"
    title="Display bootles from your cave"
    return render_template('stock.html', title = title, page_title = page_title)   

#Display bottles whicjh need to be drink
@app.route('/to_drink/')
def to_drink():
    page_title = "Pynard"
    title="Display bootles to older"
    return render_template('to_drink.html', title = title, page_title = page_title)   




