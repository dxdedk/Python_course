import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://soware.ru/categories/clients-and-partners-search-services"
r = requests.get(URL_TEMPLATE)

soup = bs(r.text,"html.parser")
a_tags = soup.find_all('a','dEWdHg')
h1_tags = soup.find('h1')

print(len(a_tags))
print(h1_tags.text)

print(type(h1_tags))