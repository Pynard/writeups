
from pwn import *

p = remote('chal.imaginaryctf.org', 42011)

p.recvuntil('Check\n').decode()
p.recvuntil('> ').decode()
p.send(b'1\n')
p.recvuntil(': ').decode()

log.info("Sending 'fimmeflag'")
p.send(b'0'*32+binascii.hexlify(b'fimmeflag')+b'\n')

log.info("Flipping 1st byte in cipher")
cipher = binascii.unhexlify(p.recvuntil('\n')[:-1])
cipher = (cipher[0]^0b1).to_bytes(1,'little')+cipher[1:]
cipher = binascii.hexlify(cipher)

p.recvuntil('> ').decode()
p.send(b'2\n')
p.recvuntil(': ').decode()

log.info("Sending flipped cipher")
p.send(cipher+b'\n')
flag = p.recvuntil('\n').decode()
log.success('Flag = '+flag)
