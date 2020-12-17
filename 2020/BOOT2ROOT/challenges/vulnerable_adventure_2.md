# VULNERABLE_ADVENTURE_2
```Oh no! A vulnerability!(Use previous client)

Author : smcri```
Dans le code on a ça :
```python
    choice = input("Enter your choice : ")
    if choice == vuln:
        dummyflag = 1 
        
    if choice == 1 : 
        goblin = 1 
    elif choice == 2 : 
        posy = 1 
    elif choice == 3 : 
        posy = -1
    elif choice == 4 : 
        posx = -1
    elif choice == 5 : 
        posx = 1 
    elif choice == 6 : 
        terminated = 1 

    packet = struct.pack("iiiiiiii",posx,posy,coins,health,mana,goblin,terminated,dummyflag)
    #print(packet)
    s.send(packet)
```

Alors tu rentres **vuln** et là le flag pop -_-

```b00t2root{python2_vuln}```

flag : `b00t2root{python2_vuln}`

