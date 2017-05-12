import urllib.request
from bs4 import BeautifulSoup

def grabText(url): #takes html filename as input and converts it into simple text

    

    file = open(url,"r",encoding='utf-8')
    html = file.read()

    soup = BeautifulSoup(html, "html.parser")


    for s in soup(["script","style"]):
        s.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text   #returns the text file

#print(grabText("C:/Users/Ankit/DesktopCompiler Design/WebpageInput/1.html"))
