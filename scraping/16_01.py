from lxml import etree
elemento = etree.Element("Teste")
elemento.text = "teste é o texto da tag Teste"
print(etree.tostring(elemento))

print(elemento.tag)


# pip install lxml

