#!usr/bin/env python

import os
import time

def write_log(file_name, log_text):
    
    file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "log" + os.path.sep + file_name, "a")
    file.write(time.strftime('%d/%y %H:%M:%S', time.localtime()) + ' | ' + log_text + '\n')
    file.close()
    return True
