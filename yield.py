#! /usr/bin/python

############################################

def generator():
    for i in range(10):
        yield i

gen = generator() # return a generator

for i in gen:
    print i

############################################

def readFile():
    f = open("test.txt", "r")
    for line in f:
        yield line.strip("\n")

fgen = readFile()

for i in fgen:
    print i

############################################

############################################

def readFileUsingWith():
    with open("test.txt", "r") as f:
        for line in f:
            yield line.strip("\n")

wf = readFileUsingWith()

for i in wf:
    print i

############################################
