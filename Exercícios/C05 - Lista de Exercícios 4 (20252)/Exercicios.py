import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

# Código que substitua todas as palavras maiores que 5 caracteres por astericos (*)
x1 = re.sub("[a-zA-ZçãéÉ]{6,}", "*", txt)
print(x1)

# Código que retorne uma lista apenas das palavras que contém caracteres com acentos
for x2 in re.finditer("[a-zA-Zç]*[áéãõàÉÀ][a-zA-Zç]*", txt):
    print(x2.group())

# Código que em um único REGEX, troque as letras maiúsculas por minúsculas, e vice-versa
x3 = re.sub("[a-zA-zçéãÉ]", lambda m: m.group().swapcase(), txt)
print(x3)

# Código que retorna a posição inicial e final da maior palavra do texto
x4 = re.search(max(txt.split(), key=len).strip(","), txt)
print(x4.span())

# Código que retorna uma lista apenas com as palavras que possuam de 2 a 6 letras
for x5 in re.finditer(r"\b[A-Za-zçãéÉ]{2,6}\b", txt):
    print(x5.group())

# Código que retorna uma lista de Strings que deverão ser quebradas toda vez que for encontrada uma letra maiúscula
x6 = re.split("[A-ZÁÉ]", txt)
print(x6)

# Código que retorne todas as palavras que contenham vogais
for x7 in re.finditer("[A-Za-zç]*[AÃÉEIOUaãeéiou][A-Za-zç]*", txt):
    print(x7.group())

# Código que responda quantas letras o texto base possui
x8 = re.findall(r"[A-Za-zÁÉÍÓÚÀÂÃÊÔÕáéíóúàâãêôõçÇ]", txt)
print(len(x8))
