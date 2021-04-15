#-*- coding: utf-8 -*-

"""
* Purpose : manage pynard functionalities
* Log : 
*     * 14/04/2021 : meriadoc : Init
"""

import lib.logger as log
import lib.config as conf
import lib.db_management as db

pynard_conf = conf.get_conf('pynard.ini')
logger = log.get_logger('pynard', log.get_logger_level('debug'))
queries = conf.get_conf('queries.ini')


def set_bottle_type():
    
    logger.info('Create new bottle type')
    max_id_query=


def get_all_bottle():
    
    rows = db.execute("SELECT * FROM COUNTRIES")
    logger.debug(len(rows))
    if len(rows) > 0:
        for row in rows:
            print(row)
    return None

def set_new_countries():
    
    logger.debug('Insert countries into COUNTRIES table')
    db.execute_file(queries['name']['populate_countries'])
    rows = db.execute("SELECT * FROM COUNTRIES")
    logger.debug(len(rows))
    if len(rows) > 0:
        for row in rows:
            print(row)
    return rows
