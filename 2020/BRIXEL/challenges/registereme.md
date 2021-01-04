# REGISTERE ME

```
This program needs to be activated

Can you figure out how to do it?
```

- File : [registereme.exe](../attachements/registereme/registereme.exe)

```
$ r2 registereme.exe
[0x004011dc]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
Warning: aao experimental on 32bit binaries
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x004011dc]> s fcn.00402320
[0x00402320]> pdf
[...]
│           0x00402695      8d4dd8         lea ecx, [var_28h]
│           0x00402698      6a62           push 0x62                   ; 'b' ; 98
│           0x0040269a      51             push ecx
│           0x0040269b      ffd6           call esi
│           0x0040269d      8d55c8         lea edx, [var_38h]
│           0x004026a0      6a72           push 0x72                   ; 'r' ; 114
│           0x004026a2      52             push edx
│           0x004026a3      ffd6           call esi
│           0x004026a5      8d45a8         lea eax, [var_58h]
│           0x004026a8      6a69           push 0x69                   ; 'i' ; 105
│           0x004026aa      50             push eax
│           0x004026ab      ffd6           call esi
│           0x004026ad      8d4d88         lea ecx, [var_78h]
│           0x004026b0      6a78           push 0x78                   ; 'x' ; 120
│           0x004026b2      51             push ecx
│           0x004026b3      ffd6           call esi
│           0x004026b5      8d9568ffffff   lea edx, [var_98h]
│           0x004026bb      6a65           push 0x65                   ; 'e' ; 101
│           0x004026bd      52             push edx
│           0x004026be      ffd6           call esi
│           0x004026c0      8d8548ffffff   lea eax, [var_b8h]
│           0x004026c6      6a6c           push 0x6c                   ; 'l' ; 108
│           0x004026c8      50             push eax
│           0x004026c9      ffd6           call esi
│           0x004026cb      8d8d28ffffff   lea ecx, [var_d8h]
│           0x004026d1      6a43           push 0x43                   ; 'C' ; 67
│           0x004026d3      51             push ecx
│           0x004026d4      ffd6           call esi
│           0x004026d6      8d9508ffffff   lea edx, [var_f8h]
│           0x004026dc      6a54           push 0x54                   ; 'T' ; 84
│           0x004026de      52             push edx
│           0x004026df      ffd6           call esi
│           0x004026e1      8d85e8feffff   lea eax, [var_118h]
│           0x004026e7      6a46           push 0x46                   ; 'F' ; 70
│           0x004026e9      50             push eax
│           0x004026ea      ffd6           call esi
│           0x004026ec      8d8dc8feffff   lea ecx, [var_138h]
│           0x004026f2      6a7b           push 0x7b                   ; '{' ; 123
│           0x004026f4      51             push ecx
│           0x004026f5      ffd6           call esi
│           0x004026f7      8d95a8feffff   lea edx, [var_158h]
│           0x004026fd      6a66           push 0x66                   ; 'f' ; 102
│           0x004026ff      52             push edx
│           0x00402700      ffd6           call esi
│           0x00402702      8d8588feffff   lea eax, [var_178h]
│           0x00402708      6a31           push 0x31                   ; '1' ; 49
│           0x0040270a      50             push eax
│           0x0040270b      ffd6           call esi
│           0x0040270d      8d8d68feffff   lea ecx, [var_198h]
│           0x00402713      6a6c           push 0x6c                   ; 'l' ; 108
│           0x00402715      51             push ecx
│           0x00402716      ffd6           call esi
│           0x00402718      8d9548feffff   lea edx, [var_1b8h]
│           0x0040271e      6a33           push 0x33                   ; '3' ; 51
│           0x00402720      52             push edx
│           0x00402721      ffd6           call esi
│           0x00402723      8d8528feffff   lea eax, [var_1d8h]
│           0x00402729      6a34           push 0x34                   ; '4' ; 52
│           0x0040272b      50             push eax
│           0x0040272c      ffd6           call esi
│           0x0040272e      6a63           push 0x63                   ; 'c' ; 99
│           0x00402730      8d8d08feffff   lea ecx, [var_1f8h]
│           0x00402736      51             push ecx
│           0x00402737      ffd6           call esi
│           0x00402739      8d95e8fdffff   lea edx, [var_218h]
│           0x0040273f      6a63           push 0x63                   ; 'c' ; 99
│           0x00402741      52             push edx
│           0x00402742      ffd6           call esi
│           0x00402744      8d85c8fdffff   lea eax, [var_238h]
│           0x0040274a      6a33           push 0x33                   ; '3' ; 51
│           0x0040274c      50             push eax
│           0x0040274d      ffd6           call esi
│           0x0040274f      8d8da8fdffff   lea ecx, [var_258h]
│           0x00402755      6a73           push 0x73                   ; 's' ; 115
│           0x00402757      51             push ecx
│           0x00402758      ffd6           call esi
│           0x0040275a      8d9588fdffff   lea edx, [var_278h]
│           0x00402760      6a73           push 0x73                   ; 's' ; 115
│           0x00402762      52             push edx
│           0x00402763      ffd6           call esi
│           0x00402765      8d8568fdffff   lea eax, [var_298h]
│           0x0040276b      6a7d           push 0x7d                   ; '}' ; 125
│           0x0040276d      50             push eax
│           0x0040276e      ffd6           call esi
[...]
```

Thanks **radare2** :)

flag : `brixelCTF{f1l34cc3ss}`
