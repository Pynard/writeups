# STINGS
```
Description
Enter the beehive. Don't get stung.

(Note: the password/flag is in the format ictf{.*})

Attachments
https://2021.imaginaryctf.org/r/stings

```

- File : [stings](../attachements/stings/stings)

Here we have to type the password that is the flag

Looking in gdb we can see that the typed pwd is compared with an other string from which each is char is substracted by 1 :
```
│       ┌─< 0x0000083c      eb47           jmp 0x885
│       │   ; CODE XREF from main @ 0x88c
│      ┌──> 0x0000083e      8b85ecedffff   mov eax, dword [var_1214h]
│      ╎│   0x00000844      4898           cdqe
│      ╎│   0x00000846      0fb68405f0ed.  movzx eax, byte [rbp + rax - 0x1210]
│      ╎│   0x0000084e      0fbed0         movsx edx, al
│      ╎│   0x00000851      8b85ecedffff   mov eax, dword [var_1214h]
│      ╎│   0x00000857      4898           cdqe
│      ╎│   0x00000859      0fb68405f0ee.  movzx eax, byte [rbp + rax - 0x1110]
│      ╎│   0x00000861      0fbec0         movsx eax, al
│      ╎│   0x00000864      83e801         sub eax, 1
│      ╎│   0x00000867      39c2           cmp edx, eax
│     ┌───< 0x00000869      7413           je 0x87e
│     │╎│   0x0000086b      488d3d1e0100.  lea rdi, str.Im_disappointed._stings_you ; 0x990 ; "I'm disappointed. *stings you*"
│     │╎│   0x00000872      e859fdffff     call sym.imp.puts
│     │╎│   0x00000877      b8ffffffff     mov eax, 0xffffffff         ; -1
│    ┌────< 0x0000087c      eb21           jmp 0x89f
│    ││╎│   ; CODE XREF from main @ 0x869
│    │└───> 0x0000087e      8385ecedffff.  add dword [var_1214h], 1
│    │ ╎│   ; CODE XREF from main @ 0x83c
│    │ ╎└─> 0x00000885      83bdecedffff.  cmp dword [var_1214h], 0x22
│    │ └──< 0x0000088c      7eb0           jle 0x83e
│    │      0x0000088e      488d3d1b0100.  lea rdi, str.Congrats__The_password_is_the_flag. ; 0x9b0 ; "Congrats! The password is the flag."
│    │      0x00000895      e836fdffff     call sym.imp.puts
```

At each loop from **0x0000088c** to **0x0000083e** we need to take the jump at **0x00000869**

The current character tested is subtracted by 1 at **0x00000864**

With radare 2, here are the strings compared with the type pwd :
```
│           0x00000779      4889d7         mov rdi, rdx
│           0x0000077c      f348ab         rep stosq qword [rdi], rax
│           0x0000077f      48b86a647567.  movabs rax, 0x7375747c6775646a ; 'jdug|tus'
│           0x00000789      48ba326f6874.  movabs rdx, 0x3473356074686f32 ; '2oht`5s4'
│           0x00000793      488985f0eeff.  mov qword [var_1110h], rax
│           0x0000079a      488995f8eeff.  mov qword [var_1108h], rdx
│           0x000007a1      48b86f756069.  movabs rax, 0x346565326960756f ; 'ou`i2ee4'
│           0x000007ab      48ba6f603238.  movabs rdx, 0x623233633832606f ; 'o`28c32b'
│           0x000007b5      48898500efff.  mov qword [var_1100h], rax
│           0x000007bc      48899508efff.  mov qword [var_10f8h], rdx
│           0x000007c3      48c78510efff.  mov qword [var_10f0h], 0x7e3a37 ; '7:~'
│           0x000007ce      48c78518efff.  mov qword [var_10e8h], 0
│           0x000007d9      488d9520efff.  lea rdx, [var_10e0h]
```

A simple python script to solve the flag :

```py
flag = 'jdug|tus2oht`5s4ou`i2ee4o`28c32b7:~'
''.join([ chr(ord(elt)-1) for elt in flag ])
```

it gives us :
```
ictf{str1ngs_4r3nt_h1dd3n_17b21a69}
```

flag : `ictf{str1ngs_4r3nt_h1dd3n_17b21a69}`
