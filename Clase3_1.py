print("Diferentes maneras de usar print")
a = 0
b = 2
c = "Hola"
print(4 * "Hola")
print("Nose", "Loli", sep="/")
print("Hola", end="")
print("Que bonito el curso", "Solo que algo violento", sep="\n")
print("Probando %d %d %s" % (a, b, c))
numeroGrande = 15121861534864165
print(numeroGrande.__format__(","))

# numero = 3141.59265
#
# # Dos decimales de precisión:
# print(format(numero, '0.2f'))
#
# # Jusitificación a la derecha con diez caracteres, un decimal de precisión:
# print(format(numero, '>10.1f'))
#
# # Jusitificación a la izquierda con diez caracteres, un decimal de precisión:
# print(format(numero, '<10.1f'))
#
# # Separador de miles:
# print(format(numero, ','))
# print(format(numero, '0,.1f'))
#
# # Notación científica:
# print(format(numero, 'e'))
# print(format(numero, '0.2E'))
