import urllib.request
import re
import time
import socket
import sys

portnumber = 0
numtotal = 0
newport = 0
rhost=sys.argv[1]

def getport():
	with urllib.request.urlopen('http://'+rhost+':3010/') as url:
		urltext = url.read()
		urltextd = urltext.decode("utf-8")
	return re.findall('(?<=">).*(?=<\/a)', urltextd)

while portnumber != 1337:
	portreg = getport()
	portnumber = int(portreg[0])
	time.sleep(0.5)
print("Started.")
while 1:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((rhost, portnumber))
		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % rhost
		s.send(request.encode())
		time.sleep(0.5)
		data = s.recv(1024)
		datarepr = repr(data)
		dataregex = re.sub(r'([\\\'])+', '', datarepr)
		dataregex = re.findall('(?<=nrn).*', dataregex)
		datatrim = dataregex[0].split()
		operator = datatrim[0]
		number = float(datatrim[1])
		newport = int(datatrim[2])
		print("Operator: " + datatrim[0] + " Number: " + datatrim[1] + " New Port: " + datatrim[2])
		if(operator == 'add'):
			numtotal += number 
		elif(operator == 'minus'): 
			numtotal -= number
		elif(operator == 'multiply'):
			numtotal *= number
		elif(operator == 'divide'):
			numtotal /= number
		s.close()
		if newport == 9765:
			break
		while portnumber != newport:
			portreg = getport()
			portnumber = int(portreg[0])
			time.sleep(0.5)
	except:
		s.close()
		time.sleep(0.5)
		pass

print(numtotal)
