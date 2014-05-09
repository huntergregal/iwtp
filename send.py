#! /usr/bin/env python

from scapy.all import *

#

#ip = input("Enter first hop IP: ")
ip = IP(dst="81.4.124.11")

send(ip/UDP(sport=9013, dport=9013)/"Test data")


