tamanno = int(input("Ingrese el tamaño de la matriz: "))
filas = list()
for fila in range(0, tamanno):
    filas.clear()
    for columna in range(0, tamanno):
        filas.append(0)
    filas[fila] = 1
    print(filas)
