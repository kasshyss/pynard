#!/usr/bin/env python

import modules.create_bottle

def menu ():
    print "\n"
    print "------------------------------------"
    print "Welcome in pynard, your cave manager"
    print "What do you want to do ?"
    print "1 - add a new bottle"
    print "0 - Exit"
    return raw_input("Enter your choice : ")


def act(action):
    if action == "1":
        print "action 1"
    elif action == "0":
        print "Exit pynard"
    else:
        print "Wrong input"

action = -1

while action != "0":
    action = menu()
    act(str(action))
    print "\n"
