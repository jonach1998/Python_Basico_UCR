# Decoradores
from time import time, sleep


def debug(f):
    def nueva_funcion(*args, **kwargs):
        print(f"Funcion {f.__name__} ha sido llamada")
        return f(*args, **kwargs)
    return nueva_funcion


def timer(f):
    def nueva_funcion(*args, **kwargs):
        t = time()
        resultado = f(*args, **kwargs)
        print(f"El tiempo requerido fue de: {time() - t: .5f} segundos")
        return resultado
    return nueva_funcion


@timer
@debug
def sumar(a, b):
    sleep(0.5)
    return a + b


@timer
@debug
def multiplicar(a, b):
    sleep(1)
    return a * b


print(multiplicar(5, 7))
print(sumar(5, 7))
