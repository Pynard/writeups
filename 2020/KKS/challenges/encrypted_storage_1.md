# ENCRYPTED_STORAGE_1
On a un filesystem qu'on monte
dans le dossier 1e6947ac7fb3a9529a9726eb692c8cc5 on a un fichier chiffré qui contient un zip, on l'extrait :
```binwalk -D zip encrypted_b1a3.enc```
L'archive zip est protégée par mot de passe, on le crack avec fcrackzip :
```fcrackzip -v -u -D -p ~/rockyou.txt 4```
le mdp est **cling** :
```found file 'flag.txt', (size cp/uc     28/    16, flags 9, chk a15c)


PASSWORD FOUND!!!!: pw == cling
```
flag : `kks{n0t_s3cur3}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
