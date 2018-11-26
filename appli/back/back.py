#-*- coding: utf-8 -*-

from flask import Flask
import logging

import m_conf as conf

logger = conf.get_logger('cave_back_end', logging.DEBUG)

logger.info('Init server')

app = Flask(__name__)

logger.debug('Init done')

@app.route('/')
def index():
    logger.info('root')
    return 0
