# TAPE
```
I found this cassette tape from the '80s. I bet it has some cool games on it or something.

Better start looking for someone who grew up in that era... :)
```

- File : [CTF-TAPe.wav](../attachements/tape/CTF-TAPe.wav)

This is the recording of a tape containing a commodore 64 game.

Lets convert to a **tap** file using
[https://github.com/lunderhage/c64tapedecode](https://github.com/lunderhage/c64tapedecode)

```
c64tapedecode/src/wav2tap CTF-TAPe.wav > ctf.tap
```

Now just run it with a commodore 64 emulator

![tape.gif](../attachements/tape/tape.gif "tape.gif")

flag : `brixelCTF{BASIC}`
