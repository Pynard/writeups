# BSON
aprés avoir télécharger le fichier bson
on obtient `.£key\¤flagÜ.177/'6/l2.5/.?ll0.>)(.4=*o.%3).(.598.1o//.;9.,=?7!`  avec une passe d'hexa
aprés un passage par message pack
```json
{
    "key": 92,
    "flag": [
        55,
        55,
        47,
        39,
        54,
        47,
        108,
        50,
        3,
        53,
        47,
        3,
        63,
        108,
        108,
        48,
        3,
        62,
        41,
        40,
        3,
        52,
        61,
        42,
        111,
        3,
        37,
        51,
        41,
        3,
        40,
        46,
        53,
        57,
        56,
        3,
        49,
        111,
        47,
        47,
        28,
        59,
        57,
        3,
        44,
        61,
        63,
        55,
        33
    ]
}
```
```
['7', '7', '/', "'", '6', '/', 'l', '2', '\x03', '5', '/', '\x03', '?', 'l', 'l', '0', '\x03', '>', ')', '(', '\x03', '4', '=', '*', 'o', '\x03', '%', '3', ')', '\x03', '(', '.', '5', '9',
 '8', '\x03', '1', 'o', '/', '/', '\x1c', ';', '9', '\x03', ',', '=', '?', '7', '!']
```
```[ chr(elt) for elt in a['flag'] ]```
flag : `kks{js0n_is_c00l_but_hav3_you_tried_m3ss@ge_pack}`
GG ! Enfin un qui ne fait pas partie de ceux qui ne sont rien
<:macron:784920050544017429>
```py
''.join([ chr(elt^92) for elt in a['flag']])
```
