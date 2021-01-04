# SALTY
```
Our l33t hackers hacked a bulletin board and gained access to the database. We need to find the admin password.

The user's database info is:

Username:admin

Passwordhash:2bafea54caf6f8d718be0f234793a9be

Salt:04532@#!!


We know from the source code that the salt is put AFTER the password, then hashed. We also know the user likes to use lowercase passwords of only 5 characters long.

The flag is the plaintext password.
```

By looking at the hash length the hashing function must be md5
lets write a python bruteforce code

```python
import itertools
import hashlib
import string

pwd_hash = '2bafea54caf6f8d718be0f234793a9be'
salt = b'04532@#!!'

for key in itertools.product(string.ascii_lowercase,repeat=5):
    key = ''.join(key).encode()
    if hashlib.md5(key+salt).hexdigest() == pwd_hash:
        print('key =',key.decode())
        break
```

Response :

```
key = 'brute'
```

flag : `brixelCTF{brute}`
