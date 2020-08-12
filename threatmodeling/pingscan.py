#!/usr/bin/python

import sys
from scapy.all import *
conf.verb = 0

target = sys.argv[1]

for ip in range(1, 255):
	host = target + '.' + str(ip) 
	pack_ip = IP(dst=host)
	packt = pack_ip/ICMP()
	resp, noresp = sr(packt,timeout=1)
	for response in resp:
		print(response[1][IP].src, 'is up')


