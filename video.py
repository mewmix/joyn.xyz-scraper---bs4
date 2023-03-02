from bs4 import BeautifulSoup

with open("scrape.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

video_tags = soup.find_all("video")

print(video_tags)

print(len(video_tags))

