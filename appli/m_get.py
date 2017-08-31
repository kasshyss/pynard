#!/usr/bin/env python

import m_log
import os


#return 
def get_cave():
    print 'toto'
    try:
        file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'data' + os.path.sep + 'cave.csv', 'r')
        lines = file.readlines()
        file.close()
        cave = []
        for bottle in lines:
            cave.append(bottle[:-1:].split(';'))
        return cave

    except ValueError:
        print 'The cave dors is closed'
        m_log.write_log('appli.log', 'm_get.get_cave | ' + str(ValueError))
