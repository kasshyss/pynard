#!/usr/bin/env python

import m_log as log
import psycopg2 as pg
import m_conf as conf

#run a sql query in postgres
#return the result
#use config to connect to the rigth DB
def __pg_request(query):

    db_conf = conf.get_conf('db.conf')
    try:
        conn = pg.connect("dbname='" + str(db_conf['DB']) + "' user='" + str(db_conf['USER']) + "' host='" + str(db_conf['IP']) + "' password='" + str(db_conf['PWD']) +"'")
        cursor =  conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_IO.add_bottle_pg | Unable to manage the database link' + str(ValueError))
        return False
    return data

#Get a bootle from storage
def get_bottles():
    return __pg_request(conf.get_conf('queries.conf')['get_bottle'])

#Get a productor from storage
def get_productor():
    return __pg_request(conf.get_conf('queries.conf')['get_productor'])


#add bottle in pg
def add_new_bottle(bottle_attribute, productor_attribute):

    queries = conf.get_conf_('queries.conf')
    add_bottle_query = queries['insert_bottle']
    add_productor_query = queries['insert_productor']
    attributes_field=''
    attributes_values=''
    bottle = conf.get_label('bottle.conf')
    productor = conf.get_label('productor.conf')
    for key in bottle_attribute:
        print 'toto'
    __pg_request(add_bottle_query)
    __pg_request(add_productor_query)
    return True


