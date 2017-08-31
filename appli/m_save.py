#!/usr/bin/env python

import os
import m_log

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

