# Determinar el nombre con la longitud mas grande

lista = list()
lista.append("Valeria")
lista.append("Jonathan")
lista.append("Felipe")

valor_maximo = 0
indice_maximo = 0
nombre_maximo = 0

for indice, nombre in enumerate(lista):
    if valor_maximo < len(lista[indice]):
        indice_maximo = indice
        valor_maximo = len(lista[indice])
        nombre_maximo = nombre

print(indice_maximo, valor_maximo, nombre_maximo)
