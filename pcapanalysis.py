#def main ():
##	iterator()

class Host:
	#this is for identifying each host, their classification and it's behaviour
	def __init__(self, ip):
		self.ip = ip


	def displayip(self):







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
	print file
	a = scapy.rdpcap(file)
	a.show()
	print(a)
#	print a


for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
	if file.endswith(".pcap"):
		print(file)
		pcapanalyser(file)
