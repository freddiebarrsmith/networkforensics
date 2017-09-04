# coding: utf-8

import virustotal
import urllib

APIKEY = "6578e4386c6d850f55cbeaefd9f29fcf580f313378c794eca07bda6ec94596a8"
vTotal = virustotal.VirusTotal(APIKEY)

report = vTotal.get("66506e4e771c8b2fad384c7564b07ea6")

# Query the report
print "Report"
print "−Resources  UID: " , report.id
print "−Scans UID: ", report.scan_id
print "−Permalink : " , report.permalink
print "−Resources SHA1 : " , report.sha1
print "−Resources SHA256 : ", report.sha256
print "−Resources MD5: ", report.md5
print "−Resources status : ", report.status
print "−Antivirus total : ", report.total
print "−Antivirus positives :", report.positives
for antivirus , malware in report:
    if malware is not None :
      print
      print " Antivirus : " , antivirus[0]
      print " Antivirus version: " , antivirus[1]
      print " Antivirus update: " , antivirus[2]
      print "Malware: ", malware
