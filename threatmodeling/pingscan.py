#!/usr/bin/python

import sys
from scapy.all import *
conf.verb = 0

target = sys.argv[1]
count = 0
for ip in range(1, 255):
	host = target + '.' + str(ip) 
	print('scanning', host)
	pack_ip = IP(dst=host)
	packt = pack_ip/ICMP()
	resp, noresp = sr(packt,timeout=5)
	for response in resp:
		print(response[1][IP].src, 'is up')
		count += 1
print(str(count))


