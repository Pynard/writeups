# DOTTY
```
My new program will keep your secrets safe using military grade encryption!
```

- File : [Dotty.exe](../attachements/dotty/Dotty.exe)

When we run it we can translate chars to morse code :
```
Please enter your secret to encode: ABC
.-|-...|-.-.
```

Here :
```
A -> .-
B -> -...
C -> -.-.
etc...
```

By looking at strings in the binary we easily spot the flag :
```
$ strings -e l Dotty.exe
[...]
-|....|.|/|..-.|.-..|.-|--.|/|..|...|/|---|.---|--.-|-..-|.|-.--|...--|..-|--|--..|.....|.--|..|--|.-..|.|.-..|.....|....-|-|.-|.....|-.-|--...|---|.-|--..|-|--.|..---|..---|--...|--.|-...|--..|..-.|-....|-.|.-..|--.-|.--.|.|--...|-|-....|.--.|--..|--...|.-..|.....|-|--.|-.-.|-.|-..|-...|--|--|...--|-..|.-|-.|.-..|.....|/|-...|.-|...|.|...--|..---
[...]
```

The morse code gives us :
```
THE FLAG IS OJQXEY3UMZ5WIMLEL54TA5K7OAZTG227GBZF6NLQPE7T6PZ7L5TGCNDBMM3DANL5 BASE32
```

and **OJQXEY3UMZ5WIMLEL54TA5K7OAZTG227GBZF6NLQPE7T6PZ7L5TGCNDBMM3DANL5** from base32 gives us :

```
rarctf{d1d_y0u_p33k_0r_5py????_fa4ac605}
```

flag : `rarctf{d1d_y0u_p33k_0r_5py????_fa4ac605}`