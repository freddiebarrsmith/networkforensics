


import dpkt

import socket

def printPcap(pcap):

    for (ts, buf) in pcap:

        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + ' --> Dst: ' + dst
        except:
            print "failed"
            pass

def main():

    f = open('/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap/feadef3e-a62e-47d6-8eec-697af9ac22f4.pcap','rb')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)
