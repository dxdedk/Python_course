import requests
from bs4 import BeautifulSoup as bs

URL = 'https://soware.ru'
res = requests.get(URL)
if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

soup.find_all('div')
soup.find_all('div', {'class': 'class_name', 'id': 'name_id'})

soup.find('div')
soup.find('qwertyuio')

suo.select('div')