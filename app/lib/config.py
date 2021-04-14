#-*- coding: utf-8 -*-

"""
* Purspose : Manage conf files - for any purpose about conf file structure please check python doc.
* Author : Meriadoc
* Log :
    * 05/08/2019 : meriadoc : Initial commit
    * 09/08/2019 : meriadoc : update get_section error management
    * 14/04/2021 : meriadoc : add feature to reach fix folder
"""


import lib.logger as log
import configparser
import os
import pathlib

logger = log.get_logger('config', log.get_logger_level('debug'))
app_conf_path = os.path.join(pathlib.Path(__file__).parent.parent, 'config')


def get_section(file_name, section, *args, **kwargs):
	
    """
	* Purpose : return a dict of a section conf
	* Raise :
	    * TypeError
	    * IOError
	    * NameError
	    * UnicodeError
	* In : 
	    * file_name : name of the file conf
	    * path : where is stored the conf file (optional)
	    * subpath : sub localtion of the conf file (optional)
	    * section : the conf section name that you are looking for
	* Out :
	    * dict with all the conf param of the section
    """	
	
    logger.debug('Start to get conf {}'.format(file_name))
    
    path = kwargs.get('path', app_conf_path)
    sub = kwargs.get('subpath', None)
    
    
    
    
    path = path if sub is None else os.path.join(app_conf_path , sub)
    
    
    
    #San tests
    if not isinstance(section, str):
        logger.error('Parameter section has to be a string')
        raise TypeError('Wrong parameter type')

    full_name = __san_tests(file_name, path)

    try:
        logger.debug('In try') 
        config = configparser.ConfigParser()
        config.read(full_name)
        config.sections()
        
        if config.has_section(section) == False:
            logger.error('Missing section {0} in config file {1}'.format(section, full_name))
            raise IOError

        logger.debug('Conf loaded - check section')
        conf_r = config[section]

        for key, value in conf_r.iteritems():
            logger.debug('Key : {0} | Value : {1}'.format(key, value))


    except UnicodeError:
        logger.error('Fail to read file {}'.format(full_name))
        raise
    except ValueError as e:
        logger.error('Unexpected error when loading file {}'.format(full_name))
        logger.error('{}'.format(e), exec_info = True)
        raise NameError('Unexpected error')
    else:
        logger.info('Conf file {0}/{1} loaded'.format(file_name, section))
        return conf_r


def get_conf(file_name, *args, **kwargs):

    """
	* Purpose : return a dict of a conf file
	* Raise :
	    * TypeError
	    * IOError
	    * NameError
	    * UnicodeError
	* In : 
	    * file_name : name of the file conf
	    * path : where is stored the conf file (optional)
	    * subpath : sub localtion of the conf file (optional)
	* Out :
	    * dict with all the conf
    """

    logger.debug('Start to get conf {}'.format(file_name))

    path = kwargs.get('path', app_conf_path)
    sub = kwargs.get('subpath', None)
    
    path = path if sub is None else os.path.join(path , sub)

    full_name = __san_tests(file_name, path)

    try:
        config = configparser.ConfigParser()
        config.read(full_name)
        config.sections()

        logger.debug('Conf loaded')
 

    except UnicodeError:
        logger.error('Fail to read file {}'.format(full_name))
        raise
    except ValueError as e:
        logger.error('Unexpected error when loading file {}'.format(full_name))
        logger.error('{}'.format(e), exec_info = True)
        raise NameError('Unexpected error')
    else:
        logger.info('Conf file {0} loaded'.format(file_name))
        return config


def __san_tests(file_name, path):
	
    """
	* Purpose : check parameters
    """

    logger.debug('parameters sanity test')
    if not isinstance(file_name, str):
        logger.error('Parameter file_nam has to be a string')
        raise TypeError('Wrong parameter type')

    if not isinstance(path, str):
        logger.error('Parameter path has to be a string')
        raise TypeError('Wrong parameter type')
    
    full_name = os.path.join(path,  file_name)

    if not os.path.exists(full_name):
        logger.error('File {0} missing in forlder {1}'.format(file_name, path))
        raise IOError('Missing file')

    return full_name
