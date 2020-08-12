#!/usr/bin/python

import sys
from scapy.all import *

conf.verb = 1

ports = [21,22,23,25,80,443,110]

pack_ip = IP(dst=sys.argv[1])
pack_tcp = TCP(dport=ports,flags='S')
packet = pack_ip/pack_tcp
resp, noresp = sr(packet)
#resp.show()
for response in resp:
	port = response[1][TCP].sport
	flag = response[1][TCP].flags
	if  (flag == 'SA'):
		print(port, ' ', 'open')
