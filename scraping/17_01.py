from lxml import etree

funcionarios = etree.parse("funcionarios.xml")
# print(funcionarios.find("funcionario"))
print(funcionarios.getroot().find("funcionario"))