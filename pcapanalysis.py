#def main ():
##	iterator()

#main()
import dpkt, os
for file in os.listdir("/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap"):
	if file.endswith(".pcap"):
		print(file)
