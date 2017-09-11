#!/usr/bin/env python

import os, sys


cmd = 'psql -h 127.0.0.1 -d pynard -U meriadoc -f pynard_create_tables.sql'
os.system(cmd)
