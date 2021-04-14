#-*- coding: utf-8 -*-

"""
* Purpose : manage pynard functionalities
* Log : 
*     * 14/04/2021 : meriadoc : Init
"""


from flask import Flask

import lib.logger as log
import lib.config as conf

import pynard

logger = log.get_logger('pynard_app', log.get_logger_level('debug'))

logger.info('Init server')

app = Flask(__name__)

logger.debug('Init done')

@app.route('/')
def index():
    logger.info('root')
    toto = pynard.get_all_bottle()
    return "Done"
