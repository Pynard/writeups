

import itertools
import struct
import string
import crc8

crccheck = [
    0x464dd4d6,0xc73ecd53,0x8a506d41,0x8e2cbf22,
    0x55019c09,0xc5f43510,0x4fd8686b,0xa81315d5,
    0x3242d308,0xa1940654,0xffadfbe0,0x82319e5f,
    0xf21eca02,0x47e2d74a,0x14806648,0x2d27da67,
    0x1140e862,0x81842123,0xcebe1774,0x0eb5929b,
    0xf799f0c6,0x763adfa6,0xf6d17cdd,0x07b7e9a9,
    0x7ec27a97,0x304cb390,0x8545fd5d,0xf3e375a3,
    0x380dbd49,0xfab98bb4,0x2bb259aa,0xe60bcf6a,
    0xbc3c6305,0x887987e5,0x433403a5,0x897d1def,
    0xb13358f1,0x7f958378,0xf5b67bdb,0x37ba2f1b,
    0xd012188d,0x703fe773,0x640a0ca7,0xae6c719f,
    0xb896eb28,0x868f19a2,0xc9dc0fd9,0xab5e39f9,
    0x25c1cb51,0xee446520,0x1fa43b5c,0xc829afcc,
    0x61ac602a,0x4b5bf85a,0x9d8cec93,0x98dec3a0,
    0xeae436bb,0xb03d0072,0x6f774e24,0x1ac0fe52,
    0x2e566991,0x04fc169a,0x571c26e1,0xc46ed2ed]
crccheck = b''.join([ struct.pack('<I',elt) for elt in crccheck ])

crc_block = [[ hex(i)[2:] for i,elt in enumerate(crccheck) if elt == c ] for c in b'w1nR4rs' ]
crc_block = [ elt[0] for elt in crc_block ]

# bruteforce crc8
out = [None]*7
charset = string.ascii_letters

# 1st block
out[0] = b'rarctf'

# 2nd block
for test in itertools.combinations(charset.encode(),5):
    test = b'{'+bytes(test)
    crc_fx = crc8.crc8(test)
    if crc_fx.hexdigest() == crc_block[1]:
        out[1] = test 

# last block
for test in itertools.combinations(charset.encode(),5):
    test = bytes(test)+b'}'
    crc_fx = crc8.crc8(test)
    if crc_fx.hexdigest() == crc_block[-1]:
        out[-1] = test 

# other blocks
for test in itertools.combinations(charset.encode(),6):
    test = bytes(test)
    crc_fx = crc8.crc8(test)
    if crc_fx.hexdigest() in crc_block[2:-1]:
        for i,elt in enumerate(crc_block):
            if elt == crc_fx.hexdigest():
                out[i] = test 
        if all([ elt != None for elt in out]):
            break

out = b''.join(out)
print(out.decode())
