from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.folha.uol.com.br")
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a",{"href":re.compile(".*\.folha\.uol\.com\.br/mercado/2019/03/.*\.shtml")})

for link in links:
    print(link["href"])