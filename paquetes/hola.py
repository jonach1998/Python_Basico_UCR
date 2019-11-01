def miHola():
    return "Hola Jona"


def saludoPersonalizado(nombre):
    return f"Hola {nombre}"


def saludoArgumentoDefault(nombre="Felipe"):
    return f"Hola {nombre}"


def listaArgumentos(*argumentos):
    for i in argumentos:
        print(i)
