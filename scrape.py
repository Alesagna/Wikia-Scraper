import os
import requests
from bs4 import BeautifulSoup

check = os.getcwd()

def remover(insert): #REMOVES THAT STUPID WORD GARBAGE
    removal_list = ["\n","\t", "/"]

    for word in removal_list:
        insert = insert.replace(word, "")
    return insert

def Scraper(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    os.chdir(os.path.join(check, "Saved Images"))
    james = str(remover(soup.find('h1', class_ = 'page-header__title').get_text())) #james is our great friend, his jobs is to name the file where the thing will go, say thank you james ! Ale thanks james ! Dewniel thanks james !
    try:
        os.mkdir(james)
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), james))
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
