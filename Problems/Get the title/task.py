import requests
from bs4 import BeautifulSoup

url = input().strip()
article = requests.get(url)
if article.status_code == 200:
    soup = BeautifulSoup(article.content, 'html.parser')
    h1 = soup.find('h1')
    print(h1.text)
