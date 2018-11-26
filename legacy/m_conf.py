#!/usr/bin/env python

import os
import m_log as log

#NOTE : conf file is two parts : Label|Value


def get_conf(file_name):

    try:
        file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'config' + os.path.sep + file_name, 'r')  
        lines = file.readlines()
        file.close()
    except ValueError:
        print 'Unable to open the log file ' + str(file_name) + str('\n')
        log.write_log('appli.log', 'm_conf.get_conf | unable to open the conf file '+ str(file_name))
    data = {}
    for line in lines:
        data[line.split('|')[0]] = line.split('|')[1][:-1:]
    return data
