# # BABYCRYPT

![](../attachements/babycrypt/unknown.png "unknown.png")

## The problem

Let's take a look to the encryption part **server.py**. So, first the script generates 2 prime numbers **p** & **q** of 256 bits and ensures that **p** is less than **q**. Then it returns, the public exponent **e**, the modulus **n**, the ciphertext **c**, and a hint, which is **n % (q-1)**. 

```python
from Crypto.Util.number import getPrime, bytes_to_long

flag = bytes_to_long(open("/challenge/flag.txt", "rb").read())

def genkey():
    e = 0x10001
    p, q = getPrime(256), getPrime(256)
    if p <= q:
      p, q = q, p
    n = p * q
    pubkey = (e, n)
    privkey = (p, q)
    return pubkey, privkey

def encrypt(m, pubkey):
    e, n = pubkey
    c = pow(m, e, n)
    return c

pubkey, privkey = genkey()
c = encrypt(flag, pubkey)
hint = pubkey[1] % (privkey[1] - 1)
print('pubkey:', pubkey)
print('hint:', hint)
print('c:', c)
```

Let's get these numbers with the IP provided : 

```
nc 193.57.159.27 27855
```

And we get : 

```python
e = 65537
n = 9205850565099355009233119992333308509057926987587516553442010262770434065524651458723071213422539739783091104957937112504373819793996033829929775503108243
c = 7373290721518384012603108696715714033444163435512092120442505886297149465422635100860419886468382605598579995038885045596223387641682763096919583716818416

hint = 571338771748514167423682983583747408415015678000205027955504564266299803503
```

The goal is to uncipher **c** to get the flag under the form``rarctf{something}``

### The solution

Let's note ``R = hint`` for more conveniency. We have : 

**n = p\*q**

**p > q**

**n % (q - 1) = R**

In order to resolve the problem, we need to factorize **n**. So, we need to find **q** and **p**. Testing **n** in `factor.db` gives nothing. So we need do some math :

```python
n mod (q-1) = R
p*q mod (q-1) = R
[ p mod (q-1) * q mod (q-1) ] mod (q-1) =R
[ p mod (q-1) * 1 ] mod (q-1) = R
[ p mod (q-1) ] mod (q-1) = R
p mod (q-1) = R

p ~ q and q < p 
=>  p = k*(q-1) + R   where k = 1 because q ~ p
=>  p = q - 1 + R
=>  p - q = R - 1 

or n = p * q
=> n = q * (q + R -1)
=> q^2 + (R-1) * q - n = 0

Find the positive root and we have q, next we have p, next we break it lul
```

To find **q**, we need to solve the equation above. Let's use Sage to do this :

```python
sage: e = 65537                                                                                                  
sage: n = 9205850565099355009233119992333308509057926987587516553442010262770434065524651458723071213422539739783091104957937112504373819793996033829929775503108243
sage: c = 7373290721518384012603108696715714033444163435512092120442505886297149465422635100860419886468382605598579995038885045596223387641682763096919583716818416                                                                       
sage: R = 571338771748514167423682983583747408415015678000205027955504564266299803503  
sage: var('t')                                                                                                                     
sage: Pol = t^2+t*(R-1)-n 
sage: solve(Pol,t)                                                                                                                        
[t == 95661879681818872731638606929439794975150932660862158767273961317066822333587, 
 t == -96233218453567386899062289913023542383565948338862363795229465881333122137089]

sage: q = 95661879681818872731638606929439794975150932660862158767273961317066822333587
sage: p = n/q
sage: p
96233218453567386899062289913023542383565948338862363795229465881333122137089
sage: p*q == n 
True # So we have p and q !
sage: d = pow(e,-1,(p-1)*(q-1))
sage: d
7525291550178795884914566387678293738739343004806842307666643511411881291367347791355702688078467521251399949304045751083067891511306720238422997433554945
sage: m = pow(c,d,n)
sage: m
21282889459489084011886583837365850378164449578188153850335772055863288361368436716339359416861416171924194634444635934246077740557666778378
```

Converting **m** with **long_to_bytes()** function (from pycryptodome python package) and we obtain the flag:

flag : `rarctf{g3n3r1c_m4th5_equ4t10n_th1ng_ch4ll3ng3_5a174f54e6}`
