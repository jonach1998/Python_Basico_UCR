resultado = 0

operaciones = dict()
operaciones["+"] = "%d + %d"
operaciones["-"] = "%d - %d"
operaciones["*"] = "%d * %d"
operaciones["/"] = "%d / %d"

numero1 = int(input("Ingresar numero 1: "))
numero2 = int(input("Ingresar numero 2: "))
operadores = input("Elija su operador (+,-,*,/): ")

print("Su resultado es: ", eval(operaciones[operadores] % (numero1, numero2)))
