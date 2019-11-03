# Invertir lista
lista = list()
listaInvertida = list()
lista.append("Hola")
lista.append("Jona")
lista.append("Como")
lista.append("Estas")
lista.append("?")
for elemento in range(len(lista) - 1, 0 - 1, -1):
    listaInvertida.append(lista[elemento])
print(lista)
print(listaInvertida)

# Segunda manera
for crearElemento in lista:
    listaInvertida.append("*")
tamanno = len(listaInvertida) - 1
for elemento in lista:
    listaInvertida[tamanno] = elemento
    tamanno -= 1
print(listaInvertida)
