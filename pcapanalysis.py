#def main ():
##	iterator()



#main()
#from scapy import *
#import scapy
#from scapy import *
import scapy.all as scapy

#def pcapanalyser(file):
#	print file
a = scapy.rdpcap("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap/feadef3e-a62e-47d6-8eec-697af9ac22f4.pcap")
print(a)
#	print a

#for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
#	if file.endswith(".pcap"):
#		print(file)
#		pcapanalyser(file)
