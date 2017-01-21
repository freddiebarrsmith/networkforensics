import dpkt
from dpkt.ip import IP
from dpkt.ethernet import Ethernet
from dpkt.arp import ARP

f = open('/root/Desktop/mscdissforensics/pcaps/laredo-13.mit.edu/~brendan/regin/pcap/feadef3e-a62e-47d6-8eec-697af9ac22f4.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
  eth = dpkt.ethernet.Ethernet(buf)
  if eth.type != dpkt.ethernet.ETH_TYPE_IP:
    print 'Non IP Packet type not supported'
    continue

  ip = eth.data
  do_not_fragment = bool(dpkt.ip.IP_DF)
  more_fragments = bool(dpkt.ip.IP_MF)
  fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
  print 'IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
  (ip.src, ip.dst, ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset)