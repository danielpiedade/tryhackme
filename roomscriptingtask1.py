import base64

file = open("b64.txt", "r")
encoded = file.read()
for i in range(0, 50):
	encoded = base64.b64decode(encoded)
print(encoded)
