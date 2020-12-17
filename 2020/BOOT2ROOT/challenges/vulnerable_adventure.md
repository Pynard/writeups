# VULNERABLE_ADVENTURE
```
Run the client, switch the delegate, get the flag

Challenge author : smcri
```
- Fichier : [client.py](../attachements/vulnerable_adventure/client.py)
Quand on run le client on a un jeu qui se lance :
```
Welcome to game
What would you like to do?
1. Speak to goblin in front of you(2 energy) 
 2. Move Forward 1 step(1 energy) 
 3. Move Backward 1 step(1 energy) 
 4. Move Left 1 step(1 energy) 
 5. Move Right 1 step(1 energy) 
 6. Exit 
Enter your choice : 1

Go to position (9,9). A flag awaits for you!
Welcome to game
What would you like to do?
1. Speak to goblin in front of you(2 energy) 
 2. Move Forward 1 step(1 energy) 
 3. Move Backward 1 step(1 energy) 
 4. Move Left 1 step(1 energy) 
 5. Move Right 1 step(1 energy) 
 6. Exit 
```
On voit que le flag se trouve à la position (9,9)
Il suffit de faire croire au serveur qu'on est à la position du flag en modifiant la position envoyée :
```diff
-      packet = struct.pack("iiiiiiii",posx,posy,coins,health,mana,goblin,terminated,dummyflag)
+      packet = struct.pack("iiiiiiii",9,9,coins,health,mana,goblin,terminated,dummyflag)
```
Easy on a le flag :
```
b00t2root{p4ck3t_inj3ct}
```
flag : `b00t2root{p4ck3t_inj3ct}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
