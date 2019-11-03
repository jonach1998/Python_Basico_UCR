# Como saber si un numero es primo
primo = 0
valor = 1
while valor != 0:
    valor = int(input("Favor digitar el valor a determinar: "))
    if valor == 2:
        primo = 1
    else:
        for numero in range(2, valor):
            if valor % numero == 0:
                primo = 0
                break
            else:
                primo = 1
    if primo:
        print("El numero es primo ", valor)
    else:
        print("El numero no es primo ", valor)
