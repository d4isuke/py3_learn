#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

import sys

def Hello(name):
    if name == 'Alice' or name == 'Nick':
        print ('Alert: Alice or Nick Mode'.upper())
        name = name + '???'
    else:
        name = name + '!!!!'
    print ('Hello', name)
            
def main():
    if len(sys.argv[1]) == 0:
        print ('Aert: Input Name')
    else: 
        Hello(sys.argv[1])

if __name__ == '__main__':
    main()
