import requests
import re
from bs4 import BeautifulSoup

word = input().strip()
url = input().strip()

req = requests.get(url)
if req.status_code == 200:
    soup = BeautifulSoup(req.content, 'html.parser')
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        if word in p.text:
            print(p.text)
            break
