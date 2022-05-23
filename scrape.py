import os
import requests
from bs4 import BeautifulSoup


def Scraper(url):
    owd = os.gedcwd()
    os.chdir(os.path.join(os.getcwd(), "Saved Images"))
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    images = soup.find("div", class_="mw-parser-output").find_all("img", class_="thumbimage lazyload")

    for image in images:
        preImageLink = image["data-src"]
        imageKey = image["data-image-key"]
        subImageLink1 = preImageLink.split("/scale-to-width-down/", 1)
        substring1 = subImageLink1[0]
        subImageLink2 = url.split("?", 1)
        substring2 = subImageLink2[0]
        imageLink = (f"{substring1}?{substring2}")
        title = image["alt"]
        with open(title.replace(":", "-").replace("?", "-") + imageKey[-4:], "wb") as f:
            img = requests.get(imageLink)
            f.write(img.content)
   os.chdir(owd)


