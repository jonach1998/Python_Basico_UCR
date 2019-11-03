valor = int(input("Favor ingresar el valor: "))
if valor < 0:
    valor *= -1
elif valor > 0:
    valor *= 1
else:
    valor = 0
print("Numero absoluto: ", valor)
