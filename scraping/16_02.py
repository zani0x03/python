from lxml import etree

clientes = etree.Element("clientes", atributo="Valor")
cliente1 = etree.SubElement(clientes,"cliente")

nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "nome do primeiro cliente"

idade1 = etree.SubElement(cliente1, "idade")
idade1.text = "32"

clientes.insert(0,etree.Element("cliente0"))

clientes.set("codigo","1234")

print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))

#verifica se cliente é pai de clientes[1]
print(clientes is clientes[1].getparent())

print(clientes.get("codigo"))