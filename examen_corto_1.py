# Ejercicio 1
contador = {10_000: 0, 5_000: 0, 2_000: 0}


def cajero(monto):
    if monto == 0:
        return 0
    elif monto >= 10_000:
        contador[10_000] += 1
        return cajero(monto - 10_000)
    elif monto >= 5_000:
        contador[5_000] += 1
        return cajero(monto - 5_000)
    elif monto >= 2_000:
        contador[2_000] += 1
        return cajero(monto - 2_000)
    else:
        return 1


print("Ejercicio 1. Cajero")
while 1:
    contador = {10_000: 0, 5_000: 0, 2_000: 0}
    dinero = int(input("Favor ingresar el monto a dispensar: "))
    if dinero == -1:
        break
    elif dinero < 2000:
        print("Solo montos de dos mil colones (2,000) en adelante")
    else:
        error = cajero(dinero)
        if error == 1:
            print("Solo montos en combinaciones de billetes de 2,000 , 5,000 y 10,000")
        else:
            for billete, contadorBilletes in contador.items():
                if contadorBilletes != 0:
                    print(f"{contadorBilletes} de {billete: ,}")


# Ejercicio 2
print("Ejercicio 2. Palindromos")
while 1:
    palin = 0
    palabra = input("Ingrese la palabra: ")
    if palabra == "-1":
        break
    tamanno = len(palabra)
    nuevaPalabra = [0] * tamanno
    tamannoParaFor = tamanno - 1
    for posicion, letra in enumerate(palabra):
        nuevaPalabra[tamannoParaFor - posicion] = letra
    for posicion, letra in enumerate(palabra):
        if letra != nuevaPalabra[posicion]:
            palin = 0
            break
        else:
            palin = 1
    if palin:
        print("Es palindromo")
    else:
        print("No es palindromo")

# Ejercicio 3
print("Ejercicio 3. Listas")
while 1:
    comun = 0
    lista = input("Digite la primera lista: ")
    if lista == "-1":
        break
    lista1 = lista.split(",")
    lista = input("Digite la segunda lista: ")
    if lista == "-1":
        break
    lista2 = lista.split(",")
    for elemento in lista1:
        for posicion in range(len(lista2)):
            if elemento == lista2[posicion]:
                print("Elemento en comun: ", elemento)
                comun = 1
    if comun == 0:
        print("No existen elementos en comun")
