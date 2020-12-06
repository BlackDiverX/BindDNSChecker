#!/usr/bin/env python3
import socket
import re
import sys

f = open(sys.argv[1])
raw_dns_list = f.readlines()
f.close()
dnslist = []
dns_and_ip = []
for i in enumerate(raw_dns_list):
	dns_record = i[1].replace("\n","")
	dns_record = i[1].replace("\t"," ")
	finder = dns_record.find("IN A")
	if finder!=-1:
		dnslist.append(dns_record.partition('. ')[0])
dnslist = list(sorted(set(dnslist)))

for i in enumerate(dnslist):
	dnsname=""
	dnsname=i[1]
	print("Processing "+str(i[0])+" of "+str(len(dnslist)))
	try:
		ip_addr = socket.gethostbyname(dnsname)
		x=[dnsname, ip_addr]
		
		if x[0] != "localhost":
			dns_and_ip.append(x)
	except Exception:
		pass

f_good = open("good_domains_"+sys.argv[1]+"_result.txt","w")
f_bad = open(sys.argv[1]+"bad_domains_"+sys.argv[1]+"_result.txt","w")

for i in dns_and_ip:
			word = i
			regexp = re.compile(r'(^192\.168\.)|(^10\.)|(^127\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)')
			if regexp.search(i[1]):
				f_bad.write(str(i[0])+"    "+str(i[1])+"\n")
			else:
				f_good.write(str(i[0])+"\n")
f_good.close()
f_bad.close()
print("File "+sys.argv[1]+" Complete")
