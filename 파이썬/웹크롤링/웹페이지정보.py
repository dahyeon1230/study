import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
html = requests.get(url)
print(html.text)
