#!/usr/bin/env python

import os
import m_log

#NOTE : conf file is two lines
# L1 : db name
# L2 : label name

#return a list with the label of conf
def get_label(conf_file_name):
    
    file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'config' + os.path.sep + conf_file_name, 'r')
    lines = file.readlines()
    file.close()
    #m_log.write_log('appli.log', 'm_conf.get_label | ' + str(lines[1][:-2:].split(';')))
    return lines[1][:-2:].split(';')
