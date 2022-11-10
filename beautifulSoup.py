from bs4 import BeautifulSoup
from requests import get

URL = "https://google.com/"

site = get(URL)

soup = BeautifulSoup(site, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
for link in soup.find_all("img"):
    print(link.get('src'))
