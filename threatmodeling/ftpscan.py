#!/usr/bin/python

import sys
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1], 21))

banner =  tcp.recv(1024)
print(banner)

tcp.send('USER ftp\r\n')
user =  tcp.recv(1024)
print(user)

tcp.send('PASS ftp\r\n')
pw = tcp.recv(1024)
print(pw)

tcp.send('HELP \r\n')
cmd = tcp.recv(2048)
print(cmd)
_
