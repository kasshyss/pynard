#-*- coding: utf-8 -*-

"""
* Purpose : manage pynard functionalities
* Log : 
*     * 14/04/2021 : meriadoc : Init
"""


from flask import Flask
from flask import request
import json

import lib.logger as log
import lib.config as conf

import pynard

logger = log.get_logger('pynard_app', log.get_logger_level('debug'))

logger.info('Init server')

app = Flask(__name__)
config = conf.get_conf('flask.ini')

logger.debug('Init done')

@app.route('/')
def index():
    logger.info('root')
    pynard.set_bottle_type()
    return 'DONE'

@app.route('/get_bottle_type')
def get_bottle_type():
    logger.info('get bottle type')
    bottle_type = pynard.get_bottle_type()
    logger.debug(bottle_type)
    return json.dumps(bottle_type)

@app.route('/update_bottle_type')
def update_bottle_type():
    logger.info('update bottle type')
    bottle_type = {}
    bottle_type['id'] = request.args.get(config['requests.parameters']['bottle_type_id'])
    bottle_type['name'] = request.args.get(config['requests.parameters']['bottle_type_name'])
    
    if bottle_type['id'] is None or bottle_type['name'] is None:
        logger.warning('Missing parameter')
        return json.dumps('Error : missing parameter id or name')

    data = pynard.update_bottle_type(bottle_type)
    return json.dumps(data)

@app.route('/create_bottle_type')
def create_bottle_type():
    logger.info('create bottle type')
    
    type_name = request.args.get(config['requests.parameters']['bottle_type_name'])
    if type_name is None:
        logger.warning('Missing parameter')
        return json.dumps('Error : missing parameter : name is require')
    
    data = pynard.set_bottle_type(type_name)
    return json.dumps(data)

@app.route('/get_countries')
def get_countries():

    logger.info('Retrive countries list')
    data = pynard.get_countries()
    return json.dumps(data)
