# IMAGINARY
```
Description
What's ImaginaryCTF without good old sqrt(-1)?

Attachments
https://imaginaryctf.org/r/CE4D-imaginary.py nc chal.imaginaryctf.org 42015
```

- File : [imaginary.py](../attachements/imaginary/imaginary.py)
```python
#!/usr/bin/env python3

import random
from solve import solve

banner = '''
Welcome to the Imaginary challenge! I'm gonna give you 300 imaginary/complex number problems, and your job is to solve them all. Good luck!

Sample input: (55+42i) + (12+5i) - (124+15i)
Sample output: -57+32i

Sample input: (23+32i) + (3+500i) - (11+44i)
Sample output: 15+488i

(NOTE: DO NOT USE eval() ON THE CHALLENGE OUTPUT. TREAT THIS IS UNTRUSTED INPUT. Every once in a while the challenge will attempt to forkbomb your system if you are using eval(), so watch out!)
'''

flag = open("flag.txt", "r").read()
ops = ['+', '-']

print(banner)

for i in range(300):
	o = random.randint(0,50)
	if o > 0:
		nums = []
		chosen_ops = []
		for n in range(random.randint(2, i+2)):
			nums.append([random.randint(0,50), random.randint(0,50)])
			chosen_ops.append(random.choice(ops))
		out = ""
		for op, num in zip(chosen_ops, nums):
			out += f"({num[0]}+{num[1]}i) {op} "
		out = out[:-3]
		print(out)
		ans = input("> ")
		if ans.strip() == solve(out).strip():
			print("Correct!")
		else:
			print("That's incorrect. :(")
			exit()
	else:
		n = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
		payload = f"__import__['os'].system('{n}(){{ {n}|{n} & }};{{{n}}}')"
		print(payload)
		input("> ")
		print("Correct!")

print("You did it! Here's your flag!")
print(flag)
```

Here we have to solve complex equations, but we have 1/50 chance to get a forkbomb so : **no eval**

```
$ ncat chal.imaginaryctf.org 42015
Welcome to the Imaginary challenge! I'm gonna give you 300 imaginary/complex number problems, and your job is to solve them all. Good luck!

Sample input: (55+42i) + (12+5i) - (124+15i)
Sample output: -57+32i

Sample input: (23+32i) + (3+500i) - (11+44i)
Sample output: 15+488i

(NOTE: DO NOT USE eval() ON THE CHALLENGE OUTPUT. TREAT THIS IS UNTRUSTED INPUT. Every once in a while the challenge will attempt to forkbomb your system if you are using eval(), so watch out!)

(45+34i) - (37+37i)
> 8-3i
Correct!
(27+29i) + (42+40i) + (6+31i)
> 
```

Here is a script that solve the equations :

- Fichier : [exploit.py](../attachements/imaginary/exploit.py)
```python
from pwn import *

conn = remote('chal.imaginaryctf.org', 42015)

conn.recvuntil(b'out!)\n\n')

for _ in range(300):
    received = conn.recvuntil(b'\n')[:-1].decode('utf-8')
    if '__import__' in received:
        print(received)
        result = 'forkbomb\n'
    else:
        print(received,end=' = ')
        equation = received.split(' ')
        
        c = []
        operands = []
        for i,elt in enumerate(equation):
            if i%2 == 0:
                c += [complex(elt[1:-1].replace('i','j'))]
            else:
                operands += [elt]
        
        result = c[0] 
        for i,op in enumerate(operands):
            if op == '+':
                result += c[i+1]
            elif op == '-':
                result -= c[i+1]
        
        result = (result.__str__()[1:-1].replace('j','i')+'\n')
        print(result)
        
    conn.send(result.encode())
    received = conn.recvuntil(b'\n')[:-1].decode('utf-8')
    print(received)

print(conn.recvall().decode())
```

Here is the output :
```
$ python exploit.py
[...]
> Correct!
(3+8i) - (32+37i) - (29+48i) - (37+9i) + (11+3i) + (0+4i) + (48+45i) - (19+35i) - (24+1i) + (48+12i) + (38+48i) + (14+9i) + (15+50i) + (44+27i) + (39+42i) - (39+43i) - (27+4i) + (29+48i) + (18+18i) + (9+13i) - (23+6i) - (24+27i) - (27+16i) + (22+20i) + (21+34i) - (12+45i) - (21+41i) - (42+33i) + (40+16i) - (20+37i) + (42+17i) + (9+24i) + (27+10i) - (48+38i) - (35+33i) + (7+46i) + (3+41i) + (35+34i) - (7+46i) - (47+27i) - (42+50i) + (20+43i) - (30+20i) + (36+37i) + (50+41i) - (12+41i) + (27+24i) + (15+35i) - (24+20i) + (26+4i) - (18+41i) + (16+37i) - (7+18i) + (15+5i) + (2+28i) - (1+15i) + (26+16i) + (31+11i) + (25+5i) - (27+37i) - (30+28i) + (5+13i) + (35+22i) + (37+43i) - (10+14i) + (17+6i) + (41+11i) + (24+1i) + (14+36i) - (29+17i) - (36+4i) - (30+48i) - (28+42i) + (33+22i) + (39+9i) - (12+8i) - (19+32i) - (26+46i) + (36+6i) + (41+20i) - (27+17i) + (26+28i) + (2+11i) - (32+21i) + (1+36i) + (38+48i) - (24+44i) - (33+11i) + (19+24i) - (15+4i) - (44+49i) + (38+12i) - (34+9i) + (1+13i) - (17+48i) + (40+22i) - (32+13i) + (48+47i) + (47+19i) - (29+13i) + (23+44i) - (6+30i) - (46+43i) + (49+8i) - (38+22i) + (35+10i) - (35+25i) - (29+29i) - (41+11i) + (16+32i) - (50+15i) - (8+23i) - (34+34i) - (36+7i) - (44+25i) - (27+10i) - (7+43i) - (44+25i) + (17+1i) + (19+22i) - (2+7i) - (34+34i) + (16+35i) + (50+10i) + (39+20i) - (1+24i) + (36+45i) - (25+23i) + (26+46i) + (45+10i) - (49+48i) - (25+36i) - (42+33i) + (14+30i) - (28+40i) - (26+40i) + (31+1i) - (44+40i) + (26+24i) - (7+38i) + (27+42i) + (15+42i) - (10+39i) + (42+14i) + (20+15i) - (50+49i) - (40+30i) - (36+3i) + (2+3i) - (47+27i) - (4+50i) + (49+45i) - (29+38i) = -135-374i

> Correct!
[+] Receiving all data: Done (77B)
[*] Closed connection to chal.imaginaryctf.org port 42015
You did it! Here's your flag!
ictf{n1c3_y0u_c4n_4dd_4nd_subtr4ct!_49fd21bc}
```

flag : `ictf{n1c3_y0u_c4n_4dd_4nd_subtr4ct!_49fd21bc}`
