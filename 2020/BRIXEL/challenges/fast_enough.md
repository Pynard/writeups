# FAST ENOUGH

```
Can you program something that is fast enough to submit the solution before the time runs out?

http://timesink.be/speedy
```

On this page we get a code to send back via a POST method in less than 1 second

```bash
#!/bin/bash

rm index header

curl --output index -D header http://timesink.be/speedy/index.php

cookie=$(cat header | grep Cookie | cut -d ' ' -f 2 | tr -d ';')
code=$(cat index | cut -d '>' -f 13-14 | cut -d '<' -f 1)

curl -X POST --cookie "$cookie" --data-raw "inputfield=$code" http://timesink.be/speedy/index.php
```

We get this response :

```html
<html>
  <body>
    <div align="center">
      <h1>Are you fast enough?  </h1>
    </div>
    <hr>
      <div align="center">You took: 0 second(s) to complete the task.</div>
    <br>
    <div align="center">Congratulations, you completed the task in under 1 seconds!</div>
    <div algin="center">The flag is: <b>brixelCTF{sp33d_d3m0n}</b></div>
  </body>
</html>
```

flag : `brixelCTF{sp33d_d3m0n}`