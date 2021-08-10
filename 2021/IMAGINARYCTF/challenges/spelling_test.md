# SPELLING_TEST
```
Description
I made a spelling test for you, but with a twist. There are several words in words.txt that are misspelled by one letter only. Find the misspelled words, fix them, and find the letter that I changed. Put the changed letters together, and you get the flag. Make sure to insert the "{}" into the flag where it meets the format.

NOTE: the words are spelled in American English

Attachments
https://imaginaryctf.org/r/CBC8-words.txt
```

- File : [words.txt](../attachements/spelling_test/words.txt)

Here is the dictionary that i used :

- File : [google-10000-english-no-swears.txt](../attachements/spelling_test/google-10000-english-no-swears.txt)

Here is the python code to solve the challenge :

- File : [solve.py](../attachements/spelling_test/solve.py)
```python
with open('google-10000-english-no-swears.txt','r') as f:
    dictionary = f.read().split('\n')[:-1]

with open('words.txt','r') as f:
    mispelled = f.read().split('\n')[:-1]

response = ''
for word in mispelled:
    char = ''
    match = 0
    potential = ''
    for correct in dictionary:
        len_word = len(word)
        if len_word == len(correct):
            #print('+ '+correct)
            errors = sum([ mispelled_c != correct_c for mispelled_c,correct_c in zip(word,correct) ])
            if errors == 0:
                match = 0
                break
            elif errors == 1:
                potential = correct
                match += 1

            if match > 1:
                break

    if match == 1:
        for mispelled_c,correct_c in zip(word,potential):
            if mispelled_c != correct_c:
                print(mispelled_c,end='')
```

```
$ python solve.py
ictfyoupassedthespellingtest
```

flag : `ictf{youpassedthespellingtest}`