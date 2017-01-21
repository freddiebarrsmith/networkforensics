#def main ():
##	iterator()
import re
import sys
import io
#from StringIO import StringIO
import os
import scapy.all as scapy
import dpkt
import datetime
import socket

class Host:
	#this is for identifying each host, their classification and it's behaviour
	def __init__(self, ip):
		self.ip = ip


	def displayip(self):
		print (host.ip)
#also create an id for this


class Stream:
	def __init__(self, ip, host1id, host3id):
		self.ip = ip
		self.host1id = host1id
		self.host3id = host3id
		self.protocol = protocol

	#this is for identifying each connection stream 
	#automatically increment this stream by 1 each time it is instantiated





def pcapanalyser(file):
	os.chdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap")
	print
	f = open(file)
	print file
	pcap = dpkt.pcap.Reader(f)
#https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/
	for ts, buf in pcap:
		eth=dpkt.ethernet.Ethernet(buf)
#		print eth
#		ip = eth.data
#		tcp = ip.data
#		print tcp.sport
#		print tcp.dport
    	eth = dpkt.ethernet.Ethernet(buf)
    	ip = eth.data
    	tcp = ip.data
    	print tcp.dport
    	try:
	    	src = socket.inet_ntoa(ip.src)
    	except:
    		pass
    	# Mac address
    	src_mac = (eth.dst).encode("hex")
    	dst_mac = (eth.src).encode("hex")
    	smac = ':'.join([src_mac[i:i+2] for i in range(0, len(src_mac), 2)])
    	dmac = ':'.join([dst_mac[i:i+2] for i in range(0, len(dst_mac), 2)])

    	# Packet
    	ip = eth.data
    	tcp = ip.data
    	print ip.p
    	try:
	    	src = socket.inet_ntoa(ip.src)
    	except:
    		pass
    	srcport = tcp.sport
    	try:
    		dst = socket.inet_ntoa(ip.dst)
    	except:
    		pass
    	dstport = tcp.dport
    	try:
    		print dst
    	except:
    		print "dont work"

    		pass

    	try:
    		print "dont work"

    		print src
    	except:
    		pass
#    	if tcp.dport == 80 and len(tcp.data) > 0:
#        	http = dpkt.http.Request(tcp.data)
#        	print http.uri

	f.close()

for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
	if file.endswith(".pcap"):
		print(file)
		pcapanalyser(file)
