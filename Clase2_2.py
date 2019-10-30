cursos = dict()
cursos["BIE-1"] = "Calculo 1"
cursos["BIE-12"] = "Circuitos 1"
cursos["BIE-32"] = "Electronica 2"

for codigo in cursos:
    print(cursos[codigo], "El codigo del curso es:", codigo)

for llave, contenido in cursos.items():
    print(llave, contenido)
