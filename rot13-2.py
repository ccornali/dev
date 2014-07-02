import cStringIO

buf = cStringIO.StringIO()

with open('inputfile', 'r+') as infile:
    data = str(infile.read())
    buf.write(data)

    for i in data:
		if (ord(i) >= 97) and (ord(i) <= 122):
			buf.write(chr(97 + (ord(i) - 97 + 13) % 26))
		
		elif (ord(i) >= 65) and (ord(i) <= 90):
			buf.write(chr(65 + (ord(i) - 65 + 13) % 26))
			
		else:
			buf.write(ord(i))

print buf.getvalue()

buf.close()



#import cStringIO

#with open() as infile:
#	infile.read()...
