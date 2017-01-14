#def main ():
##	iterator()
import re


class Host:
	#this is for identifying each host, their classification and it's behaviour
	def __init__(self, ip):
		self.ip = ip


	def displayip(self):
		print host.ip
#also create an id for this


class Stream:
		def __init__(self, ip, host1id, host3id):
		self.ip = ip
		self.host1id = host1id
		self.host3id = host3id
		self.protocol = protocol

	#this is for identifying each connection stream 
	#automatically increment this stream by 1 each time it is instantiated





#main()
#from scapy import *
#import scapy
#from scapy import *


#class hosts


##maybe want to classify know friendly hosts


#class packets
#maybe want to classify packets


import os
import scapy.all as scapy

def pcapanalyser(file):
	os.chdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap")
#	print file
	a = scapy.rdpcap(file)
#	a.show()
	print(a)
#	print a


for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
	if file.endswith(".pcap"):
#		print(file)
		pcapanalyser(file)


