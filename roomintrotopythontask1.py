import base64

file = open("encodedflag.txt", "r")
encoded = file.read()
for i in range(0, 5):
	encoded = base64.b16decode(encoded)
for i in range(0, 5):
	encoded = base64.b32decode(encoded)
for i in range(0, 50):
	encoded = base64.b64decode(encoded)
print(encoded)
