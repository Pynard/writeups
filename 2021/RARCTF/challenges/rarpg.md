# RARPG
```
I've been building a brand new Massively(?) Multiplayer(?) Online Role-Playing(?) Game(?) - try it out! Just don't try and visit the secret dev room...

If you do not have the linked libraries, download rarpg-libs.zip and extract the libraries into your working directory. Then use
LD_LIBRARY_PATH=$(pwd) ./client <ip> <port>
```

- File : [client](../attachements/rarpg/client)

## Client Analysis
Here we have a client for an ascii game\
The goal is to get to the "dev zone"

Looking at the game we have 3 types of tile :

- walkable
- teleporter (X)
- wall (~ or W)
```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                X                                                                                           │
│                                                                                                            │
│         ~~~~~~~~~~~~~~~      WWWWWW                                                                        │
│X        ~~~~~~~~~~~~~~~      W   XW                                                                        │
│         ~~~~~~~~~~~~~~~      WWWWWW                                                                        │
│     *                                                                                                      │
│                X                                                                                           │
│                                                                                                            │
```
You are the **\***

Being through all teleporters it seems that we are interested by the one enclosed by **W**

Looking at the client, there is an interesting function **sym.move_okay_int\_\_int\_**
```
┌ 116: sym.move_okay_int__int_ (int64_t arg1, int64_t arg2);
│           ; var int64_t var_11h @ rbp-0x11
│           ; var int64_t var_10h @ rbp-0x10
│           ; var uint32_t var_ch @ rbp-0xc
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg2 @ rsi
│           0x00404970      55             push rbp                    ; move_okay(int, int)
│           0x00404971      4889e5         mov rbp, rsp
[...]
│           0x004049ba      8945f4         mov dword [var_ch], eax
│           0x004049bd      837df420       cmp dword [var_ch], 0x20
│           0x004049c1      b101           mov cl, 1
│           0x004049c3      884def         mov byte [var_11h], cl
│       ┌─< 0x004049c6      0f840a000000   je 0x4049d6
│       │   0x004049cc      837df458       cmp dword [var_ch], 0x58
│       │   0x004049d0      0f94c0         sete al
│       │   0x004049d3      8845ef         mov byte [var_11h], al
│       │   ; CODE XREF from move_okay(int, int) @ 0x4049c6
│       └─> 0x004049d6      8a45ef         mov al, byte [var_11h]
│           0x004049d9      2401           and al, 1
│           0x004049db      0fb6c0         movzx eax, al
│           0x004049de      4883c420       add rsp, 0x20
│           0x004049e2      5d             pop rbp
└           0x004049e3      c3             ret
```

Here two **cmp** are important @ 0x004049bd and 0x004049cc
The first check if we want to move the player to an empty tile : **0x20 = ' '** \
The second one check if we are going to a teleporter : **0x58 = 'X' **

## Communication analysis
To analyse communication between client and server, I have slightly modified a simple udp replay python script from [here](https://github.com/EtiennePerot/misc-scripts/blob/master/udp-relay.py) (Thx to EtiennePerot) :

- File : [udp-relay.py](../attachements/rarpg/udp-relay.py)
```python
#!/usr/bin/env python
# Super simple script that listens to a local UDP port and relays all packets to an arbitrary remote host.
# Packets that the host sends back will also be relayed to the local UDP client.
# Works with Python 2 and 3

import sys, socket
import parser
import importlib

# Whether or not to print the IP address and port of each packet received
debug=False

def fail(reason):
    sys.stderr.write(reason + '\n')
    sys.exit(1)

if len(sys.argv) != 2 or len(sys.argv[1].split(':')) != 3:
    fail('Usage: udp-relay.py localPort:remoteHost:remotePort')

localPort, remoteHost, remotePort = sys.argv[1].split(':')

try:
    localPort = int(localPort)
except:
    fail('Invalid port number: ' + str(localPort))
try:
    remotePort = int(remotePort)
except:
    fail('Invalid port number: ' + str(remotePort))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', localPort))
except:
    fail('Failed to bind on port ' + str(localPort))

knownClient = None
knownServer = (remoteHost, remotePort)
sys.stdout.write('All set, listening on '+str(localPort)+'.\n')
while True:
    importlib.reload(parser)
    data, addr = s.recvfrom(32768)
    if knownClient is None or addr != knownServer:
        if debug:
            print("")
        knownClient = addr

    if debug:
        print("Packet received from "+str(addr))

    if addr == knownClient:
        if debug:
            print("\tforwording tO "+str(knownServer)) 

        s.sendto(parser.parse(data,True), knownServer)
    else:
        if debug:
            print("\tforwarding to "+str(knownClient))
        s.sendto(parser.parse(data,False), knownClient)
```

And a parser dynamically imported to manipulate packets.\
Thanks to this we can see that packets with the map are sent from the server to the client.

So one way to solve this challenge is to manipulate the map for the player to be able to walk to the "dev teleporter"
The parser is very simple :

- File : [parser.py](../attachements/rarpg/parser.py)
```python
import binascii

def parse(data,out):
    if len(data) != 198:
        return data

    if out:
        print('--> ',end='')
    else:
        print('<-- ',end='')

    data = data.replace(b'W',b' ')
    print(data)

    return data
```

Now the teleporter is free to walk on :
```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                X                                                                                           │
│                                                                                                            │
│         ~~~~~~~~~~~~~~~                                                                                    │
│X        ~~~~~~~~~~~~~~~          X                                                                         │
│         ~~~~~~~~~~~~~~~                                                                                    │
│           *                                                                                                │
│                X                                                                                           │
│                                                                                                            │
```

and we get the flag :
```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│*                                                                                                           │
│    rarctf{g4m3_h4ck1ng_f0r_n00b5!-75f8b0}                                                                  │
│                                                                                                            │
│                                                                                                            │
```

flag : `rarctf{g4m3_h4ck1ng_f0r_n00b5!-75f8b0}`