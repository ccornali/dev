import string
import re

data = raw_input("Enter string:")
n = ""

for i in data:

	if ord(i) >= 97 and ord(i) <= 122:
		n += chr(97 + (ord(i) - 97 + 13) % 26)
		
	elif ord(i) >= 65 and ord(i) <= 90:
		n += chr(65 + (ord(i) - 65 + 13) % 26)

	else:
		n += i

print n

