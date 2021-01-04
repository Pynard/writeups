# ANDROID

```
This little android app requires a password, can you find it?

the flag is the password
```

- Fichier : [brixelCTF.apk](../attachements/android/brixelCTF.apk)

unzip brixelCTF.apk

```
$ strings classes* | grep brixel
t/tmp/1602666767984_0.27958933214667514-0/youngandroidproject/../src/appinventor/ai_kevin_erna/brixelCTF/Screen1.yail
t/tmp/1602666767984_0.27958933214667514-0/youngandroidproject/../src/appinventor/ai_kevin_erna/brixelCTF/Screen2.yail
t/tmp/1602666767984_0.27958933214667514-0/youngandroidproject/../src/appinventor/ai_kevin_erna/brixelCTF/Screen3.yail
,Lappinventor/ai_kevin_erna/brixelCTF/R$anim;
,Lappinventor/ai_kevin_erna/brixelCTF/R$attr;
,Lappinventor/ai_kevin_erna/brixelCTF/R$bool;
-Lappinventor/ai_kevin_erna/brixelCTF/R$color;
-Lappinventor/ai_kevin_erna/brixelCTF/R$dimen;
0Lappinventor/ai_kevin_erna/brixelCTF/R$drawable;
*Lappinventor/ai_kevin_erna/brixelCTF/R$id;
/Lappinventor/ai_kevin_erna/brixelCTF/R$integer;
.Lappinventor/ai_kevin_erna/brixelCTF/R$layout;
.Lappinventor/ai_kevin_erna/brixelCTF/R$mipmap;
.Lappinventor/ai_kevin_erna/brixelCTF/R$string;
-Lappinventor/ai_kevin_erna/brixelCTF/R$style;
1Lappinventor/ai_kevin_erna/brixelCTF/R$styleable;
+Lappinventor/ai_kevin_erna/brixelCTF/R$xml;
'Lappinventor/ai_kevin_erna/brixelCTF/R;
3Lappinventor/ai_kevin_erna/brixelCTF/Screen1$frame;
-Lappinventor/ai_kevin_erna/brixelCTF/Screen1;
3Lappinventor/ai_kevin_erna/brixelCTF/Screen2$frame;
-Lappinventor/ai_kevin_erna/brixelCTF/Screen2;
3Lappinventor/ai_kevin_erna/brixelCTF/Screen3$frame;
-Lappinventor/ai_kevin_erna/brixelCTF/Screen3;
	brixelCTF
+brixelCTF{th3_4ndr0ids_y0u_4r3_l00k1ng_f0r}
```

flag : `brixelCTF{th3_4ndr0ids_y0u_4r3_l00k1ng_f0r}`