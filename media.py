import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

with open("scrape.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

image_divs = soup.find_all("div", {"class": "prompt-submission-card"})

for i, image_div in enumerate(image_divs):
    image = image_div.find("img")
    src = image["src"]
    extension = os.path.splitext(urlparse(src).path)[1]
    filename = f"image_{i}{extension}"
    path = os.path.join("media", filename)
    response = requests.get(src)
    with open(path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

