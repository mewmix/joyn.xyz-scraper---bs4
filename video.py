import os
import requests
from bs4 import BeautifulSoup

with open("scrape.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

video_tags = soup.find_all("video")

for video in video_tags:
    source_tag = video.find("source")
    src = source_tag["src"]
    response = requests.get(src)

    # Create the videos directory if it doesn't exist
    if not os.path.exists("videos"):
        os.makedirs("videos")

    # Get the file name from the URL
    file_name = src.split("/")[-1]
    file_path = os.path.join("videos", file_name)

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Saved {file_name}")

