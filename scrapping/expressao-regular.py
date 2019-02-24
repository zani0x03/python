import re

texto = "Esta uma aula de Python. Esta é uma aula sobre expressões regulares."

# padrao = "Esta" -- Palavra padrão

# padrao = "."
# resultado = re.search(padrao,texto,re.DOTALL) -- considera o enter um caractere válido
# resultado = re.search(padrao,texto) -- não considera o enter um caracter válido

# padrao = "^Esta" -- encontra pois está no começo da frase
# padrao = "^uma" -- não encontra pois não está no começo da frase
# resultado = re.search(padrao,texto)

# padrao = "regulares.$" -- encontra pois está no final do texto
# padrao = "sobre$" -- não encontra pois não está no final do texto
# resultado = re.search(padrao,texto)

# padrao = "[aeiou]" -- procura ocorrências com os caracteres
# padrao = "[a-z]" -- procura ocorrências minúculas
# resultado = re.search(padrao, texto) -- retorna a primeira ocorrência
# resultado = re.findall(padrao,texto)

# padrao = "a*" -- exibe onde tiver a e onde não tiver vai colocar vazio;
# padrao = "a+" --> uma ou mais ocorrência de a, só exibirá onde tiver a;
# padrao = "\d" --> números no texto;
# padrao = "\D" --> tudo que não seja número;
# padrao = "\s" --> todo caractere que seja de espaçamento;
# padrao = "\S"  -> todo caractere que não seja de espaçamento;
# padrao = "\w" --> alfanumérico, número e sublinhado;
# padrao = "\w" --> o inverso, qualquer caractere que não seja alfanumérico; número e sublinhado;
# padrao = "\d{}" chave qtd de caracteres por exemplo \d{1} traz 1...2...3...4 \d{2} traz 10...20...30
 # padrao = "(a) | (\d)" --> () grupo de expressões e o |(ou lógico) ;
#pythex.org site para testar expressões regulares
#regex101.com/#python

#print(resultado)
# print(resultado)

# if resultado:
#     print(resultado.group())
# else:
#     print("resultado não encontrado")