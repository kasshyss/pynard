#-*- coding: utf-8 -*-

"""
* Purpose : manage logger
* Log : 
*     * 24/07/2019 : meriadoc : Init
*     * 14/04/2021 : meriadoc : add dico to avoid duplication
"""


import logging
import inspect

loggers = {}

def get_logger(name, level):
    global loggers
    if loggers.get(name):
        return loggers.get(name)
        
    logger_formatter = '%(asctime)s | %(levelname)s | %(name)s.%(funcName)s : %(message)s'

    if level not in (10,20,30,40,50):
        return False

    if not isinstance(name, str):
        return False

    logger = logging.getLogger(name)
    logger.setLevel(level)

    sh = logging.StreamHandler()
    formatter = logging.Formatter(logger_formatter)

    sh.setLevel(level)
    sh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.propagate = False
    
    logger.info('{0} : Logger {1} created'.format(inspect.stack()[0][3], name))
    loggers[name] = logger
    
    return logger

def get_logger_level(level):

    if level == 'debug':
        return logging.DEBUG
    elif level == 'warning':
        return logging.WARNING
    elif level == 'error':
        return logging.ERROR
    else:
        return logging.INFO
