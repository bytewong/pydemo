#! /usr/bin/python

#test_dict.items() returns a list combined of (key,value)
tmp = sorted(test_dict.items(),key = lambda x:x[1]) # sort (key,value) by value

name = [x[0] for x in tmp]
count = [x[1] for x in tmp]
