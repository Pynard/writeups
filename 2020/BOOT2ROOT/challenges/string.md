# STRING
```
Given an encrypted message, rasput1n encodes it the following way:

Removes the median letter of the word from the original word and appends it to the end of the encrypted word and repeats the process until there are no letters left.

A median letter in a word is the letter present in the middle of the word and if the word length is even, the median letter is the left one out of the two middle letters.

Can you decode the string?
```
Le message chiffré
- Fichier : [file](../attachements/string/file)
Un script qui le déchiffre :
```python
with open('file','r') as f:
    cipher = f.read()

out=''
for c in cipher[::-1]:
    out = out[:int(len(out)/2)]+c+out[int(len(out)/2):]

print(out)
```
- Fichier : [solve.py](../attachements/string/solve.py)
Le message déchiffré :
```
Rasputin was born to a peasant family in the Siberian village of Pokrovskoye in the Tyumensky Uyezd of Tobolsk Governorate (now Yarkovsky District of Tyumen Oblast). He had a religious conversion experience after taking a pilgrimage to a monastery in 1897. He has been described as a monk or as a 'strannik' (wanderer or pilgrim), though he held no official position in the Russian Orthodox Church. He traveled to St. Petersburg in 1903 or the winter of 1904–1905, where he captivated some church and social leaders. He became a society figure and met Emperor Nicholas and Empress Alexandra in November 1905. In late 1906, Rasputin began acting as a healer for the imperial couple's only son, Alexei, who suffered from hemophilia. The flag is b00t2root{@The_Director_is_the_bot}. He was a divisive figure at court, seen by some Russians as a mystic, visionary, and prophet, and by others as a religious charlatan. The high point of Rasputin's power was in 1915 when Nicholas II left St. Petersburg to oversee Russian armies fighting World War I, increasing both Alexandra and Rasputin's influence. Russian defeats mounted during the war, however, and both Rasputin and Alexandra became increasingly unpopular. In the early morning of 30 December [O.S. 17 December] 1916, Rasputin was assassinated by a group of conservative noblemen who opposed his influence over Alexandra and Nicholas. Historians often suggest that Rasputin's scandalous and sinister reputation helped discredit the tsarist government and thus helped precipitate the overthrow of the Romanov dynasty a few weeks after he was assassinated. Accounts of his life and influence were often based on hearsay and rumor.```
et le flag :)
```b00t2root{@The_Director_is_the_bot}```
flag : `b00t2root{@The_Director_is_the_bot}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
