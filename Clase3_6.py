numeroInicial = int(input("Ingrese el numero inicial: "))
numeroFinal = int(input("Ingrese el numero final: "))

for numero in range(numeroInicial + 1, numeroFinal, +1):
    if numero % 2 == 0:
        print(numero)
# Prueba
