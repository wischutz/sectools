#!/usr/bin/python

import socket
import sys
import re


if len(sys.argv) < 3 or len(sys.argv) > 4:
	print('USE:','python', 'smtpscan.py','target_ip_address', 'path_to_wordlist', 'port (optional, default is 25)')
	sys.exit(0)

file = open(sys.argv[2])

default_port = 25
port = int(sys.argv[3]) if len(sys.argv) == 4  else default_port 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],port))
banner = tcp.recv(1024).decode()
print('SERVICE BANNER \r\n')
print(banner + '\r\n')
print('Testing for users from provided wordlist: \r\n')
count = 0
for line in file:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((sys.argv[1],25))
	banner = tcp.recv(1024).decode()
	vrfy = ('VRFY '+line).encode()
	tcp.send(vrfy)
	res = tcp.recv(1024).decode()
	if re.search('252', res):
		count += 1
		user = res.split(' ',4)
		print(user[-1])
print(count, 'users were found from wordlist provided.')



