from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://evaldowolkers.wordpress.com")
bsObj = BeautifulSoup(html, "html.parser")

# teste = bsObj.findAll("", {"class":"comments-link"})

# for a in teste:
#     print(a)

# python = bsObj.findAll(text="Python")
# for a in python:
#     print(a)

#print(bsObj.get_text()) # retorna todo o texto da página
#print(bsObj.title) #retorna primeira ocorrÊncia da tag informada
#print(bsObj.title.name) #retorna nome da primeira ocorrência da tag informada
#print(bsObj.title.string)#retorna o texto da tag informada

#print(bsObj.title.parent) #exibe a próxima tag externa
#print(bsObj.title.parent.name) #exibe o nome da próxima tag externa
#print(bsObj.body['class'])#retorna todos os valores do atriuto informado
#print(bsObj.button['aria-controls'])
#print(bsObj.find(id="menu-item-147"))#retorna a tag que possua o id informado
