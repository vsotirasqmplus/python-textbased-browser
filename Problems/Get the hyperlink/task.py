import requests

from bs4 import BeautifulSoup

link_id = int(input().strip())
url = input().strip()

req = requests.get(url)
if req.status_code == 200:
    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.find_all('a')
    print(links[link_id -1]['href'])
