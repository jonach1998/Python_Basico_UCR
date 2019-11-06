from random import randint


def listaAleatorios(n):
    listar = [0] * n
    for i in range(n):
        listar[i] = randint(0, 100)
    return listar


lista = listaAleatorios(10)
print(lista)
for i in range(0, len(lista), +1):
    for j in range(i + 1, len(lista), +1):
        if lista[j] < lista[i]:
            temporal = lista[i]
            lista[i] = lista[j]
            lista[j] = temporal
print(lista)
