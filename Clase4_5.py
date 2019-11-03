# Determinar los primos de 2 hasta n
primo = 1
valor = 1
while valor != 0:
    valor = int(input("Favor digitar el valor a determinar: "))
    for numero in range(2, valor):
        for cadaNumero in range(2, numero):
            resultado = numero % cadaNumero
            if resultado == 0:
                primo = 0
                break
            else:
                primo = 1
        if primo:
            print(numero)
