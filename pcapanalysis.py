#def main ():
##	iterator()
import re
import sys
import io
#from StringIO import StringIO
import os
import scapy.all as scapy
import dpkt

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





#main()
#from scapy import *
#import scapy
#from scapy import *


#class hosts


##maybe want to classify know friendly hosts


#class packets
#maybe want to classify packets


collectionofpcaps = []
capture = io.StringIO()
save_stdout = sys.stdout
sys.stdout = capture


def captureparser(value, collectionofpcaps):

	print (type(value))
	collectionofpcaps.append(value)
	return collectionofpcaps

def pcapanalyser(file, collectionofpcaps):
	os.chdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap")
#	print file
	a = scapy.rdpcap(file)
	b = a.show()
	sys.stdout = save_stdout
	print ("\n" * 4)

	value = capture.getvalue()
	captureparser(value, collectionofpcaps)
	return collectionofpcaps
#	for line in b:
#		print line
#	print(a)
#	print a

#def 


for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
	if file.endswith(".pcap"):
#		print(file)
		pcapanalyser(file, collectionofpcaps)
print ("\n" * 4)

print ("value of pcap")
print (collectionofpcaps[0])
print ("\n" * 4)

c = len(collectionofpcaps)
print(c)
for elements in collectionofpcaps:
	a = type(elements)
	print(a)
	b = len(elements)
	print(b)