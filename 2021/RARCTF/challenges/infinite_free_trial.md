# INFINITE_FREE_TRIAL
```
We've decided to make an app specially for flag hoarding, can you make sure no one can crack it?

NOTE: The flag is a valid registration key
```

- File : [ift.zip](../attachements/infinite_free_trial/ift.zip)

This is a small application in trial mode asking us the registration key

## REGISTRATION
### CRC8 check
A crc check by block of 6 chars is done on the key for 6 blocks so the key must be 36 chars.

```
┌ 148: sym.do_crc_check (int64_t arg1);
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_5h @ rbp-0x5
│           ; var signed int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           0x00002c9a      55             push rbp
│           0x00002c9b      4889e5         mov rbp, rsp
│           0x00002c9e      4883ec20       sub rsp, 0x20
│           ; DATA XREF from sym.step_timer @ 0x24df
│           0x00002ca2      48897de8       mov qword [var_18h], rdi    ; arg1
│           0x00002ca6      c745fc000000.  mov dword [var_4h], 0
│       ┌─< 0x00002cad      eb49           jmp 0x2cf8
│       │   ; CODE XREF from sym.do_crc_check @ 0x2cfc
│      ┌──> 0x00002caf      8b55fc         mov edx, dword [var_4h]
│      ╎│   0x00002cb2      89d0           mov eax, edx
│      ╎│   0x00002cb4      01c0           add eax, eax
│      ╎│   0x00002cb6      01d0           add eax, edx
│      ╎│   0x00002cb8      01c0           add eax, eax
│      ╎│   0x00002cba      4863d0         movsxd rdx, eax
│      ╎│   ; DATA XREF from sym.register_tm_clones @ 0x2334
│      ╎│   0x00002cbd      488b45e8       mov rax, qword [var_18h]
│      ╎│   0x00002cc1      4801d0         add rax, rdx
│      ╎│   0x00002cc4      be06000000     mov esi, 6
│      ╎│   0x00002cc9      4889c7         mov rdi, rax
│      ╎│   0x00002ccc      e8f1feffff     call sym.crc8
│      ╎│   0x00002cd1      8845fb         mov byte [var_5h], al
│      ╎│   0x00002cd4      0fb645fb       movzx eax, byte [var_5h]
│      ╎│   0x00002cd8      4898           cdqe
│      ╎│   0x00002cda      488d153f0400.  lea rdx, obj.crccheck       ; 0x3120
│      ╎│   0x00002ce1      0fb61410       movzx edx, byte [rax + rdx]
│      ╎│   0x00002ce5      8b45fc         mov eax, dword [var_4h]
│      ╎│   0x00002ce8      4898           cdqe
│      ╎│   0x00002cea      488d0daf2400.  lea rcx, obj.crcout         ; 0x51a0
│      ╎│   0x00002cf1      881408         mov byte [rax + rcx], dl
│      ╎│   0x00002cf4      8345fc01       add dword [var_4h], 1
│      ╎│   ; CODE XREF from sym.do_crc_check @ 0x2cad
│      ╎└─> 0x00002cf8      837dfc06       cmp dword [var_4h], 6
│      └──< 0x00002cfc      7eb1           jle 0x2caf
│           0x00002cfe      ba07000000     mov edx, 7
│           0x00002d03      488d053a0500.  lea rax, [0x00003244]       ; "w1nR4rs"
│           ; DATA XREF from entry0 @ 0x22d8
│           0x00002d0a      4889c6         mov rsi, rax
│           0x00002d0d      488d058c2400.  lea rax, obj.crcout         ; 0x51a0
│           0x00002d14      4889c7         mov rdi, rax
│           0x00002d17      e8d4f3ffff     call sym.imp.memcmp
│           0x00002d1c      85c0           test eax, eax
│       ┌─< 0x00002d1e      7507           jne 0x2d27
│       │   0x00002d20      b801000000     mov eax, 1
│      ┌──< 0x00002d25      eb05           jmp 0x2d2c
│      ││   ; CODE XREF from sym.do_crc_check @ 0x2d1e
│      │└─> 0x00002d27      b800000000     mov eax, 0
│      │    ; CODE XREF from sym.do_crc_check @ 0x2d25
│      └──> 0x00002d2c      c9             leave
└           0x00002d2d      c3             ret
```

We can see that the crc of a block is used as an offset in a table **obj.crccheck** and the output is in **obj.crcout**
So : 
```
crcout[i] = crccheck[CRC8(key[i:i+6])]
```

and **crcout** must be equal to `w1nR4rs` to pass the memcmp @ 0x00002d17 and return 1

Here is a small script solving a key that passes the CRC check, this is not the flag but it will allow us to debug the second verification stage

- File : [solve_crc.py](../attachements/infinite_free_trial/solve_crc.py)
```python
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
```

Giving us : `rarctf{RUXYZabceRSabceRUabceEKabcezWMUVXZ}`

### XOR check
Here a XOR is done between 6 chars block and is compared with the **obj.xorcheck** table :

```
┌ 161: sym.do_xor_check (int64_t arg1);
│           ; var int64_t var_18h @ rbp-0x18
│           ; var signed int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           0x00002d2e      55             push rbp
│           0x00002d2f      4889e5         mov rbp, rsp
│           0x00002d32      4883ec20       sub rsp, 0x20
│           0x00002d36      48897de8       mov qword [var_18h], rdi    ; arg1
│           0x00002d3a      c745fc000000.  mov dword [var_4h], 0
│       ┌─< 0x00002d41      eb56           jmp 0x2d99
│       │   ; CODE XREF from sym.do_xor_check @ 0x2d9d
│      ┌──> 0x00002d43      8b55fc         mov edx, dword [var_4h]
│      ╎│   0x00002d46      89d0           mov eax, edx
│      ╎│   0x00002d48      01c0           add eax, eax
│      ╎│   0x00002d4a      01d0           add eax, edx
│      ╎│   0x00002d4c      01c0           add eax, eax
│      ╎│   0x00002d4e      4898           cdqe
│      ╎│   0x00002d50      488d15692400.  lea rdx, obj.xorout         ; 0x51c0
│      ╎│   0x00002d57      4801c2         add rdx, rax
│      ╎│   0x00002d5a      8b45fc         mov eax, dword [var_4h]
│      ╎│   0x00002d5d      8d4801         lea ecx, [rax + 1]
│      ╎│   0x00002d60      89c8           mov eax, ecx
│      ╎│   0x00002d62      01c0           add eax, eax
│      ╎│   0x00002d64      01c8           add eax, ecx
│      ╎│   0x00002d66      01c0           add eax, eax
│      ╎│   0x00002d68      4863c8         movsxd rcx, eax
│      ╎│   0x00002d6b      488b45e8       mov rax, qword [var_18h]
│      ╎│   0x00002d6f      488d3401       lea rsi, [rcx + rax]
│      ╎│   0x00002d73      8b4dfc         mov ecx, dword [var_4h]
│      ╎│   0x00002d76      89c8           mov eax, ecx
│      ╎│   0x00002d78      01c0           add eax, eax
│      ╎│   0x00002d7a      01c8           add eax, ecx
│      ╎│   0x00002d7c      01c0           add eax, eax
│      ╎│   0x00002d7e      4863c8         movsxd rcx, eax
│      ╎│   0x00002d81      488b45e8       mov rax, qword [var_18h]
│      ╎│   0x00002d85      4801c8         add rax, rcx
│      ╎│   0x00002d88      b906000000     mov ecx, 6
│      ╎│   0x00002d8d      4889c7         mov rdi, rax
│      ╎│   0x00002d90      e8a8feffff     call sym.xor_block
│      ╎│   0x00002d95      8345fc01       add dword [var_4h], 1
│      ╎│   ; CODE XREF from sym.do_xor_check @ 0x2d41
│      ╎└─> 0x00002d99      837dfc05       cmp dword [var_4h], 5
│      └──< 0x00002d9d      7ea4           jle 0x2d43
│           0x00002d9f      ba24000000     mov edx, 0x24               ; '$'
│           0x00002da4      488d05750400.  lea rax, obj.xorcheck       ; 0x3220 ; "\t\x16\x17\x0f\x17V\x16D:\x18So\x14\x03*\x06o1\x1cG*\x06-_Q\x1b"
│           0x00002dab      4889c6         mov rsi, rax
│           0x00002dae      488d050b2400.  lea rax, obj.xorout         ; 0x51c0
│           0x00002db5      4889c7         mov rdi, rax
│           0x00002db8      e833f3ffff     call sym.imp.memcmp
│           0x00002dbd      85c0           test eax, eax
│       ┌─< 0x00002dbf      7507           jne 0x2dc8
│       │   0x00002dc1      b801000000     mov eax, 1
│      ┌──< 0x00002dc6      eb05           jmp 0x2dcd
│      ││   ; CODE XREF from sym.do_xor_check @ 0x2dbf
│      │└─> 0x00002dc8      b800000000     mov eax, 0
│      │    ; CODE XREF from sym.do_xor_check @ 0x2dc6
│      └──> 0x00002dcd      c9             leave
└           0x00002dce      c3             ret
```

The main loop is done 6 times and the xor block is done in the **xor_block** function.

Now we can see that the first step was not necessary because the flag can be recover with the **xorcheck** table if the first key block is known..... -_-

Yet the first key block is known : `rarctf`
Here is a script that solve the xor check from **xorcheck** table

- File : [solve_xor.py](../attachements/infinite_free_trial/solve_xor.py)
```python
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
```

Giving us : `rarctf{welc0m3_t0_y0ur_new_tr14l_281099b9}`

flag : `rarctf{welc0m3_t0_y0ur_new_tr14l_281099b9}`