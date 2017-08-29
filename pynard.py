#!/usr/bin/env python

def menu ():
    print "\n"
    print "------------------------------------"
    print "Welcome in pynard, your cave manager"
    print "What do you want to do ?"
    print "1 - add a bottle(s)"
    print "2 - drink a bottle(s)"
    print "3 - check my stock"
    print "4 - bottle which need to be drink"
    print "0 - Exit"
    return raw_input("Enter your choice : ")


def act(action):
    if action == "1":
        print "add to the stock"
    elif action == "2":
        print "remove bottle(s) from the stock"
    elif action == "3":
        print "display all / a subset"
    elif action == "4":
        print "display bottles which need to be drink"
    elif action == "0":
        print "Exit pynard"
    else:
        print "Wrong input"

action = -1

while action != "0":
    action = menu()
    act(str(action))
    print "\n"
