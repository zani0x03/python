# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import requests
# html = urlopen("https://www.tudogostoso.com.br")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br'}
page = requests.get("https://www.tudogostoso.com.br", headers = headers)
soup = BeautifulSoup(page.text, "html.parser")
links =  soup.findAll("a", {"href":re.compile("/categorias/\d*")})
# links =  soup.findAll("a")
for link in links:
    print(link["href"])

    # if "href" in link.attrs:

# req = Request("https://www.tudogostoso.com.br/",headers=headers)
# html = urlopen(req).read()
# print(html)
