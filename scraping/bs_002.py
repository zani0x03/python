from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# html = urlopen("http://www.uol.com.br")
# print(html)

# try:
#     html2 = urlopen("http://www.udemy.com")
#     print(html2)
# except HTTPError as error:
#     print(error)

# try:
#     html3 = urlopen("http://www.jhgjhghjg.com/asdfasdfasdfdasfsd")
#     print(html3)
# except URLError as error:
#     print(error)    

# try:
#     html3 = urlopen("http://www.uol.com.br")
#     bsObj = BeautifulSoup(html3.read(),"html.parser")
#     resultado = bsObj.tag_nao_existente.tag
#     print(resultado)
# except AttributeError as error:
#     print(error)

# html3 = urlopen("http://www.uol.com.br")
# bsObj = BeautifulSoup(html3.read(),"html.parser")
# if bsObj.tag_nao_existete is not None:



print("teste tiago")