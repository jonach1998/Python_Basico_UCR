# Determinar cual indice tiene el valor maximo en la suma de ambos terminos

# Forma 1

lista = (2, 3), (5, -1), (8, 4), (10, -12)

valor_maximo = 0
indice_maximo = 0

for indice, valores in enumerate(lista):
    suma = lista[indice][0] + lista[indice][1]
    if valor_maximo < suma:
        valor_maximo = suma
        indice_maximo = indice

print(lista)
print(indice_maximo, valor_maximo)

# Forma 2

for indice, valores in enumerate(lista):
    suma = sum(valores)
    if valor_maximo < suma:
        valor_maximo = suma
        indice_maximo = indice

print(lista)
print(indice_maximo, valor_maximo)
