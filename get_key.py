#! /usr/bin/python
# simple script to exercise python file io and split function
import sys

for line in open(sys.argv[1], "r"):
        keys = line.split("\t")
        items = keys[0].split("+")
        if len(items) == 2:
                newKey = str(items[0]) + str(items[1])
                newLine = newKey + keys[1]
                print newLine
