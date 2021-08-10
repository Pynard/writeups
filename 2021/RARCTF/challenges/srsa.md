# SRSA

![](../attachements/srsa/unknown.png "unknown.png")

## The problem

Let's take a look at the encryption part **script.py**.

```python
from Crypto.Util.number import *

p = getPrime(256)
q = getPrime(256)
n = p * q
e = 0x69420

flag = bytes_to_long(open("flag.txt", "rb").read())
print("n =",n)
print("e =", e)
print("ct =",(flag * e) % n)
```

This script return the public exposant **e**, the modulus **n** and the ciphertext **ct**, available in the file **output.txt**.

```python
n = 5496273377454199065242669248583423666922734652724977923256519661692097814683426757178129328854814879115976202924927868808744465886633837487140240744798219
e = 431136
ct = 3258949841055516264978851602001574678758659990591377418619956168981354029697501692633419406607677808798749678532871833190946495336912907920485168329153735
```

So the encryption is very weak, we just need to solve `a.x mod n = b`

## The solution

In order to solve the equation we use the [extended Euclid algorithm]([Extended Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)) since **e** and **n** are coprime. So, let's deduce (**u**,**v**) the coefficients of Bézout's identity for **e** and **n**.

```python
=> e.u + v.n = 1
=> e.u = 1 mod n
```

So, we have the **u**, **v** and the following equation :

```python
flag*e = ct (mod n)
```

By multiplying each side of the equation by **u**, we can deduce :

```python
flag*e*u = ct*u (mod n)
=> flag*1 = ct*u (mod n)
=> flag = ct*u (mod n)
```

Let's use Sage to retrieve the plaintext message **flag** :

```python
sage: n = 5496273377454199065242669248583423666922734652724977923256519661692097814683426757178129328854814879115976202924927868808744465886633837487140240744798219                                                                       
sage: e = 431136                                                                                                                                                                                                                           
sage: ct = 3258949841055516264978851602001574678758659990591377418619956168981354029697501692633419406607677808798749678532871833190946495336912907920485168329153735
```

```python
sage: d,u,v = xgcd(e,n)                                                                                                                                                                                                                    
sage: d == 1                                                                                                                                                                                                                               
True
sage: u                                                                                                                                                                                                                                    
-1725247189852515711279864525532647026154903796685788213770661838344404757104307750862079297955287780203101052841872201379045584949770011924247049469852408

sage: flag = (ct*u).mod(n)                                                                                                                                                                                                                 
sage: flag                                                                                                                                                                                                                                 
23400784433379515514791798696357028880636218612551319923630440360753870806366867070053302757958493331539502806645178113396322834087874834615580297017725
```

Using python, let's apply **long_to_bytes()** function (from pycryptodome python package) to this final number, an we obtain :

flag : `rarctf{ST3GL0LS_ju5t_k1dd1ng_th1s_w4s_n0t_st3g_L0L!_83b7e829d9}`
