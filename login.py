#! /usr/bin/python

import paramiko
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("./account.ini")

usrname = cf.get("user_info", "username")
passwd = cf.get("user_info", "password")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = "localhost", port = 22, username = usrname, password = passwd)


cmds = ["ps -ef | grep hello_world1", "ps -ef | grep hello_world2"]

for cmd in cmds:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()
    print result

ssh.close()
