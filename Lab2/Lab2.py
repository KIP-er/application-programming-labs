import requests
from bs4 import BeautifulSoup
import os

url = "https://books.toscrape.com/"
headers = {
    "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    "AppleWebKit/537.36 (KHTML, like Gecko)"
                    "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9"
}

response=requests.get(url, headers=headers)
html = response.text
bs=BeautifulSoup(html,"lxml")
imgs=bs.find_all("img", limit=40)

os.makedirs('images', exist_ok=True)
for index, img in enumerate(imgs):
    src=img.get('src')
    if not src:
        continue
    src_clean=src.rstrip('/')
    image_url=f'{url}{src_clean}'
    print(image_url)
    jpg=f'{index}.jpg'
    