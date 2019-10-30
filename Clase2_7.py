valor = 1
while valor != 0:
    valor = int(input("Favor digite un valor distinto de 0: "))
    if valor == 0:
        break
    elif valor % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
