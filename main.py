import cv2
import os
import shutil
import requests
from PIL import Image
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

# url1 = 'https://yandex.ru/images/search?text=tiger'
# url2 = 'https://yandex.ru/images/search?text=leopard'

def get_size_image(name, i):
    im = Image.open(f"dataset/tmp_{name}/{i:04d}.jpg")
    (width, height) = im.size
    return width, height

def download_image(image_url, name, i):
    with open(f"dataset/tmp_{name}/{i:04d}.jpg", "wb") as f:
        im = requests.get(f"https:{image_url}")
        f.write(im.content)
    image = cv2.imread(f"dataset/tmp_{name}/{i:04d}.jpg")
    if get_size_image(name, i) == (1, 1):
        print('ааааааа')
        return

    cv2.imwrite(f'dataset/{name}/{i:04d}.jpg', image)
    os.remove(f"dataset/tmp_{name}/{i:04d}.jpg")


def get_image_url(name):
    i = 1
    page = 0
    os.mkdir(f"dataset/{name}")
    os.mkdir(f"dataset/tmp_{name}")
    response = requests.get(f"https://yandex.ru/images/search?p={page}&text={name}&lr=51&rpt=image", headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all('img')
    while True:
        for image in images:
            image_url = image.get('src')
            if i > 999:
                break
            if image_url != "":
                download_image(image_url, name, i)
                i += 1
        if i > 999:
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
