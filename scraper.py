import os
import requests
from bs4 import BeautifulSoup

url1 = 'https://yandex.ru/images/search?text=tiger'
url2 = 'https://yandex.ru/images/search?text=leopard'
response = requests.get(url1)
soup = BeautifulSoup(response.text, 'lxml')




