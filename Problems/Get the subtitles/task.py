import requests

from bs4 import BeautifulSoup
index = int(input().strip())
url = input().strip()
r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    h2 = soup.find_all('h2')
    print(h2[index].text)
