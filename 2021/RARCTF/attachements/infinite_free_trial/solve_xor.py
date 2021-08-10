
import struct

xorcheck = [
0x0f171609,0x44165617,0x6f53183a,0x062a0314,
0x471c316f,0x5f2d062a,0x46001b51,0x5504004a,
0x4c015066,0x526e3177,0x00737234,0x3b031b01]
xorcheck = b''.join([ struct.pack('<I',elt) for elt in xorcheck ])

key = 'rarctf'

for i,elt in enumerate(xorcheck[:0x24]):
    key += chr(ord(key[i])^elt)
print(key)

