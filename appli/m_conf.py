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
    
    bottle_list = []
    for line in lines:
        bottle_list.append(line.split('|')[1][:-1:])
    #m_log.write_log('appli.log', 'm_conf.get_label | ' + str(lines[1][:-2:].split(';')))
    return bottle_list

#get dico label / db name
def get_db_name(conf_file_name):

    file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'config' + os.path.sep + conf_file_name, 'r')
    lines = file.readlines()
    file.close()
    conf_dic={}
    for line in lines:
        conf_dic[line.split('|')[1][:-1:]] = line.split('|')[0]
    #m_log.write_log('appli.log', 'm_conf.get_db_name | ' + str(conf_dic))
    return conf_dic

def get_queries():
    try:
        file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'config' + os.path.sep + 'queries.conf', 'r')
        lines = file.readlines()
        file.close()
    except ValueError:
        print 'Unable to open the conf queries file : \n' + ValueError
        m_log.write('appli.log', 'm_conf.get_queries | Error when getting queries for the app : ' + str(ValueError))

    conf_dic={}
    for line in lines:
        conf_dic[line.split('#')[0]] = line.split('#')[1][:-1:]
    return conf_dic
