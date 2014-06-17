import cStringIO
import sys

buf = cStringIO.StringIO()

ORD_A = ord('A')
ORD_Z = ord('Z')
ORD_a = ord('a')
ORD_z = ord('z')

with sys.stdin as inf:
    data = inf.read()
    for i in data:
        ord_i = ord(i)
        if ord_i >= ORD_A and ord_i <= ORD_Z:
            buf.write(chr(ORD_A + (ord_i - ORD_A + 13) % 26))
        elif ord_i >= ORD_a and ord_i <= ORD_z:
            buf.write(chr(ORD_a + (ord_i - ORD_a + 13) % 26))
        else:
            buf.write(i)

print buf.getvalue()

buf.close()
