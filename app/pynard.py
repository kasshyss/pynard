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

def get_bottle_type():

    logger.info('Get bootle type data')
    data = db.execute_file(queries['name']['get_bottle_type'])
    if len(data) == 0:
        logger.warning('Query return no result')
    return data

def update_bottle_type(bottle_type):

    logger.info('Update bottle type {0} with new value {1}'.format(bottle_type['id'], bottle_type['name']))
    inject_data = {}
    inject_data[queries['labels']['bottle_type_id']] = bottle_type['id']
    inject_data[queries['labels']['bottle_type_name']] = bottle_type['name']

    data = db.execute_file(queries['name']['update_bottle_type'], override = inject_data)
    logger.debug('query return : {}'.format(data))
    return data

def set_bottle_type(type_name):
    
    logger.info('Create new bottle type')
    override = {}
    override['{id}'] = 'TYPE_ID'
    override['{table}'] = 'BOTTLE_TYPE'
    
    new_id = db.execute_file(queries['name']['get_max_id'], override = override)[0][0] + 1
    logger.debug('new id : {}'.format(new_id))
    type_data = {}
    type_data[queries['labels']['bottle_type_id']] = str(new_id)
    type_data[queries['labels']['bottle_type_name']] = type_name
    data = db.execute_file(queries['name']['set_bottle_type'], override = type_data)
    return data
