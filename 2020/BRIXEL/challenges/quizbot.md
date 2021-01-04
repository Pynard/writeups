# QUIZBOT

```
Legend has it there's a flag at the end when you have a perfect score

http://timesink.be/quizbot
```

On this page we have to answer to 1000 questions !

Gladly when your answer is wrong, the right answer is given with the next question.

So lets write a bot that gathers all questions + answers in a dict and then play the quiz with them.

```python
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


url = 'http://timesink.be/quizbot/index.php'
post_data = {'insert_answer':' ', 'submit':'answer'}
quiz = {}

###

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html_text = response.text
cookies = response.cookies.get_dict()
soup = BeautifulSoup(html_text,'html.parser')
question = soup.find(name='h4').text

with tqdm(range(1000),desc='Downloading questions + answers') as pbar:
    for i in pbar:
        response = requests.post(url, cookies=cookies, data=post_data, headers={'User-Agent': 'Mozilla/5.0'})
        html_text = response.text
        
        soup = BeautifulSoup(html_text,'html.parser')
        answer = soup.find(name='div',attrs={'id':'answer'}).text
        quiz[question] = answer
        if i != 999:
            question = soup.find(name='h4').text
        pbar.update(1)


###

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html_text = response.text
cookies = response.cookies.get_dict()
soup = BeautifulSoup(html_text,'html.parser')
question = soup.find(name='h4').text

with tqdm(range(1000),desc='Pwn quiz') as pbar:
    for i in pbar:
        post_data['insert_answer'] = quiz[question]
        response = requests.post(url, cookies=cookies, data=post_data, headers={'User-Agent': 'Mozilla/5.0'})
        html_text = response.text
        
        soup = BeautifulSoup(html_text,'html.parser')
        if i != 999:
            question = soup.find(name='h4').text

        pbar.update(1)
print(html_text)
```
And thew we get the flag

```html
<div align="center">Correct!</div>
Congratulations, you have defeated the mighty QuizB0t, your flag is: brixelCTF{kn0wl3dg3}
```
flag : `brixelCTF{kn0wl3dg3}`
