# Calculadora version 1
datos = input("Digite los terminos necesarios: ")
elementos = datos.split(" ")
# print(elementos)
total = int(elementos.pop(0))
tamano = len(elementos)
# print(total)
contador = 0

while contador < tamano:
    operador = elementos[contador]
    contador += 1
    siguientenumero = int(elementos[contador])
    if operador == "+":
        total += siguientenumero
    if operador == "-":
        total -= siguientenumero
    if operador == "*":
        total *= siguientenumero
    if operador == "/":
        total /= siguientenumero
    contador += 1
print(total)
