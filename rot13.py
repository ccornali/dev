import cStringIO
import sys

buf = cStringIO.StringIO()

data = sys.stdin.read()

for i in data:
    if ord(i) >= 97 and ord(i) <= 122:
        buf.write(chr(97 + (ord(i) - 97 + 13) % 26))
    elif ord(i) >= 65 and ord(i) <= 90:
        buf.write(chr(65 + (ord(i) - 65 + 13) % 26))
    else:
        buf.write(ord(i))
print buf.getvalue()

buf.close()
