#-*- coding: utf-8 -*-

"""
* Purpose : manage connection between app and db
* Log : 
*     * 14/04/2021 : meriadoc : Init
"""

import lib.logger as log
import lib.config as conf

import os
import datetime

import pathlib
import sqlite3

logger = log.get_logger('db_management', log.get_logger_level('debug'))
conf_db = conf.get_conf('db.ini')

folder = pathlib.Path(__file__).parent.parent
default_path = os.path.join(folder, conf_db['db.connection']['folder'], conf_db['db.connection']['name'])

def create_connection(*args, **kwargs):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    logger.debug('create connection')
    
    db_file = kwargs.get('db_file', default_path)
    
    logger.debug('db_file : {}'.format(db_file))    
    
    conn = None
    
    
    try:
        conn = sqlite3.connect(db_file)
        
    except Exception as e:
        logger.error('Unable to create connector to database {0}'.format(conf_db['db.connection']['name']))
        logger.error('{}'.format(e))

    return conn
    
def execute(query):
    
    logger.debug("Performe new query : {}".format(query))
    
    init_time = datetime.datetime.now()
    conn = create_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(query)
        end_time = datetime.datetime.now()
        logger.info("query performed in {} sec".format((end_time - init_time).seconds))
        
    except Exception as e:
        logger.error('Unable to perfom query on database {0}'.format(conf_db['db.connection']['name']))
        logger.debug(query)
        logger.error('{}'.format(e))
    
    return cur.fetchall()
