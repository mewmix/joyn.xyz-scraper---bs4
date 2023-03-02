import os
import requests
from bs4 import BeautifulSoup

with open("scrape.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

image_divs = soup.find_all("div", {"class": "prompt-submission-card"})

for image_div in image_divs:
    contributor_img = image_div.find("img", {"class": "rounded-full"})
    if contributor_img is not None:
        continue

    image = image_div.find("img")
    src = image["src"]
    response = requests.get(src)

    # Create the media directory if it doesn't exist
    if not os.path.exists("media"):
        os.makedirs("media")

    # Get the file name from the URL
    file_name = src.split("/")[-1]
    file_path = os.path.join("media", file_name)

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Saved {file_name}")
    print(f"src: {src}")
    print(f"file_path: {file_path}")


