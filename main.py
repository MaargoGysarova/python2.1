import os, shutil
import requests
from bs4 import BeautifulSoup
HEADERS = {"User-Agent": "Mozilla/5.0"}

# url1 = 'https://yandex.ru/images/search?text=tiger'
# url2 = 'https://yandex.ru/images/search?text=leopard'
def download_image(image_url, name, i):
    with open(f"dataset/{name}/{i:04d}.jpg", "wb") as f:
        im = requests.get(f"https:{image_url}")
        f.write(im.content)

def get_image_url(name):
    i = 1
    page = 0
    os.mkdir(f"dataset/{name}")
    response = requests.get(f"https://yandex.ru/images/search?p={page}&text={name}&lr=51&rpt=image" , headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all('img')
    while(True):
       for image in images:
          image_url = image.get('src')
          if (i > 999):
              break
          if (image_url != ""):
              download_image(image_url,name,i)
              i += 1
       if (i > 999):
           break
       page += 1

def clear_folder(name):
    shutil.rmtree(name)

def cheak_folder():
    try:
        os.mkdir("dataset")
    except:
        clear_folder("dataset")
        os.mkdir("dataset")

cheak_folder()
get_image_url("tiger")
get_image_url("leopard")