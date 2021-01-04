# EVIDENCE

```
A buddy of mine is in serious trouble. He works for the feds and accidentally deleted a pendrive containing crucial evidence

Can you get it back and tell us what the evidence is?

We need to know what the suspect bought
```

- File : [evidence.zip](../attachements/evidence/evidence.zip)

First we unzip the archive to find an img file :

```
$ file evidence.img
evidence.img: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 63, heads 255, dos < 4.0 BootSector (0x0), FAT (1Y bit by descriptor); NTFS, sectors/track 63, physical drive 0x80, sectors 1880044, $MFT start cluster 78335, $MFTMirror start cluster 2, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 0a6822852822828ef; contains bootstrap BOOTMGR
```

This img seems corrupted, as shown with fdisk :

```
$ fdisk -l evidence.img
Périphérique   Amorçage   Début      Fin  Secteurs Taille Id Type
evidence.img1  1920221984 3736432267 1816210284   866G 72 inconnu
evidence.img2  1936028192 3889681299 1953653108 931,6G 6c inconnu
evidence.img3           0          0          0     0B  0 Vide
evidence.img4    27722122   27722568        447 223,5K  0 Vide
```

We'll use **photorec** to recover some deleted files and we get 2 wav files :

```
$ ls recup_dir.1
f0011328.wav  f0028304.wav
```

- [f0011328.wav](../attachements/evidence/f0011328.wav)
- [f0028304.wav](../attachements/evidence/f0028304.wav)

These are phone calls between Dorfmeister and a bot

We have to recover DTMF key press :

```
$ multimon-ng -a DTMF -t wav f0011328.wav
```

We get :

```
212555424054666916092533266500018449903336667770844330222666222244466330227778844#2
```

Some are numbers others are multi-tap letters, so lets convert it to text to see what we've got :

```
A ALGAG JGOW M WAJEANJ THX FOR THE COCAINE BRUH
```

So he clearly bought cocaine

flag : `brixelCTF{cocaine}`