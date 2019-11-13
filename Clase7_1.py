# Recursividad

# Exponenciacion entera
# Si b > 0 entonces a**(b)*a**(b-1)..., pero si b = 0, entonces a = 1


def expo(a, b):
    if b > 0:
        return a * expo(a, b - 1)
    else:
        return 1


def expoEficiente(a, b):
    if (b > 0) and (b % 2 == 0):
        return expoEficiente(a, b / 2) * expoEficiente(a, b / 2)
    elif (b > 0) and (b % 2 != 0):
        return a * expoEficiente(a, b - 1)
    else:
        return 1


print(2 ** 6)
print(expo(2, 6))
print(expoEficiente(2, 6))
