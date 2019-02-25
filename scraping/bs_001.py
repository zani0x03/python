from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://localhost:8000/teste2.html")

html = urlopen("https://www.python.org")


bsOjb = BeautifulSoup(html.read(), "html.parser")

# print(bsOjb.html.body.h1)
# print(bsOjb.body.h1)
# print(bsOjb.html.h1)
# print(bsOjb.h1)

# print(bsOjb.find_all("h1"))
# print(bsOjb.find_all("a"))
for link in bsOjb.find_all("a"):
    # print(link)
    print(link.get("href"))