#! /usr/bin/python

import pexpect
import sys

child = pexpect.spawn('localhost 4730')

fout = file('mylog.txt','w')
child.logfile_read = fout

index = child.expect("Escape character")

if index == 0:
    child.sendline("status")
    child.expect("queue")
    
    child.sendcontrol("]")
    child.expect("telnet")
    
    child.sendline("quit")
    
    print "match"
else:
    print "not match"

child.expect(pexpect.EOF)
fout.close()
