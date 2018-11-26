#-*- coding: utf-8 -*-

import logging


# Generate logger
# get 
#     * logger name (string)
#     * logger level (Logger Enum)
# return
#     * logger (logging)
def get_logger(name, level):

    if level not in (10, 20, 30, 40, 50):
        return False
    
    if not isinstance(name, str):
        return False
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(levelname)s | %(name)s : %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('logger created')
    
    return logger
