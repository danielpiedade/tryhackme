import socket
import sys
import hashlib
import re
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

port = 4000
rhost = sys.argv[1]

def decrypt(key, iv, text, tag):
	cipherdecrypt = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend = default_backend()).decryptor()
	return cipherdecrypt.update(text) + cipherdecrypt.finalize()

while 1:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((rhost, port))
		request = input("Type hello\n")
		s.send(request.encode())
		data = s.recv(1024)
		print(repr(data)+"\n")
		request = input("Type ready\n")
		s.send(request.encode())
		data = s.recv(1024)
		key = str.encode(re.findall(r'(?<=key:)[A-Za-z0-9]+', str(data))[0])
		iv = str.encode(re.findall(r'(?<=iv:)[A-Za-z0-9]+', str(data))[0])
		checksum = data[104:136].hex()
		print(repr(data)+"\n")
		request = input("Type final\n")
		while 1:
			s.send(request.encode())
			text = bytes(s.recv(1024))
			s.send(request.encode())
			tag = bytes(s.recv(1024))
			plaintext = decrypt(key, iv, text, tag)
			if hashlib.sha256(plaintext).hexdigest() == checksum:
				print("\nThe flag is: "+ str(plaintext))
				break
		break
	except:
		s.close()
		pass
