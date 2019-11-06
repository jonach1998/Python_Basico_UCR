from random import randint
from time import time


def listaAleatorios(n):
    listar = [0] * n
    for i in range(n):
        listar[i] = randint(0, 100)
    return listar


# lista = [5, 0, 1, 0, 2]
# print(lista)
# Tiene un error, cuando se repiten los numeros deja de ordenar
# for cantidadVeces in range(len(lista)):
#     for cadaNumero, cadaElemento in enumerate(lista):
#         numeroAnterior = lista[cadaNumero - 1]
#         if cadaElemento == lista[0]:
#             continue
#         elif cadaElemento < numeroAnterior:
#             temporal = numeroAnterior
#             lista[cadaNumero - 1] = cadaElemento
#             lista[cadaNumero] = temporal

# Optimizado, basado en: https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja
lista = listaAleatorios(15)
print(lista)
for i in range(1, len(lista), +1):
    for j in range(0, len(lista) - i, +1):
        if lista[j] > lista[j + 1]:
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temporal
print(lista)
