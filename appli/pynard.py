#!/usr/bin/env python

from flask import Flask, render_template, request
import m_save
import m_conf
import m_log

app = Flask(__name__)
page_title = "Pynard"

#Application start point
@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
@app.route('/home/')
def index():
    title="Welcome in pynard, your cave manager"
    #[label, targed page]
    options_label = [["Add bottles", "add"],["Remove bottles", "remove"],["Display the stock", "stock"],["Display the bottles which nee to be drink", "to_drink"]]
    return render_template('index.html', options_label = options_label, title = title, page_title = page_title)

#Application add bottle point
@app.route('/add/', methods=['GET', 'POST'])
def add_bottle():
    bottle = m_conf.get_label('bottle.conf')
    if request.method == 'GET':
        title="Add new bootles to your cave"
        return render_template('add.html', title = title, page_title = page_title, bottle = bottle)
    else:
        bottle_attribute_dic = {}
        for attribute in bottle:
            bottle_attribute_dic[attribute] = request.form[attribute]
        m_save.add_bottle(bottle_attribute_dic)
        title="Bottle added !"
        return render_template('add.html', title = title, page_title = page_title)   

#Application remove from the stock
@app.route('/remove/')
def rm_bottle():

    title="Remove bootles to your cave"
    return render_template('remove.html', title = title, page_title = page_title)    

#Display the stock
@app.route('/stock/')
def stock():

    title="Display bootles from your cave"
    return render_template('stock.html', title = title, page_title = page_title)   

#Display bottles whicjh need to be drink
@app.route('/to_drink/')
def to_drink():

    title="Display bootles to older"
    return render_template('to_drink.html', title = title, page_title = page_title)   




