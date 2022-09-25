import os, shutil
import requests
from bs4 import BeautifulSoup

url1 = 'https://yandex.ru/images/search?text=tiger'
url2 = 'https://yandex.ru/images/search?text=leopard'
# response = requests.get(url1)
# soup = BeautifulSoup(response.text, 'lxml')

os.mkdir("dataset")
os.mkdir("dataset/" + "tiger")
os.mkdir("dataset/" + "leopard")

# images = soup.find_all('img')

def get_image_url(name):
    i = 1
    page = 0
    response = requests.get("https://yandex.ru/images/search?p={page}&text={name}&lr=51&rpt=image")
    data = []
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all('img')
    while(True):
       for image in images:
          image_url = image.get('src')
          data.append([image_url])
          if (image_url != ""):
              print("Cool")
              i += 1
          if (i > 999): break
          page += 1

def download_image(image_url,name,i):
 with open("dataset/name/'{i:04d}.jpg','wb") as f:
     im=requests.get(image_url)
     f.write(im.content)

def clear_folder(name):
    shutil.rmtree(name)
