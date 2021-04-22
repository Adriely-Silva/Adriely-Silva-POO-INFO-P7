import random
lista  = []

while (len(lista) < 6):
    x = random.randint(1,61)
    if x not in lista:
        lista.append(x)

lista_ordenada = sorted(lista)

print(lista_ordenada)

