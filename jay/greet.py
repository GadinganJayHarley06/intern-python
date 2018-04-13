#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("  ")
    if name == '': name = ''
 
print ("What's up", name, )