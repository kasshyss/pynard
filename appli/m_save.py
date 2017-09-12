#!/usr/bin/env python

import os
import m_log
import psycopg2 as pg
import m_conf as conf

#get a list of the attribute and a list of the value
#return true if all is ok
def add_bottle(bottle_attribute):
    
    m_log.write_log('appli.log', "m_save.addbottle | create bootle with " + str(bottle_attribute))
    attributes=''
    for key in bottle_attribute:
        attributes = attributes + ";" + bottle_attribute[key]
    
    path = os.path.dirname(os.path.abspath(__file__))
    
    file = open(path + os.path.sep + "data"+os.path.sep+"cave.csv", "a")
    file.write(attributes[1::]+'\n')
    file.close()
    return True

#update a bottle 
#for futur perceptives
def change_bottle_ref():
    return True

#add bottle in pg
def add_bottle_pg(bottle_attribute, productor_attribute):
    queries = conf.get_queries()
    add_bottle_query = queries['insert_bottle']()
    add_productor_query = queries['insert_productor']()
    attributes=''
    try:
        conn = pg.connect("")
        cursor =  conn.cursor()
        cursor.excute(add_bottle_query)
        cursor.excute(add_productor_query)
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_save.add_bottle_pg | Unable to manage the database link' + str(ValueError))
        return False
    return True


