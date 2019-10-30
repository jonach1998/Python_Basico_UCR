ano = int(input("Indique el año: "))

# Primero opcion

if ano % 4 == 0:
    if ano % 100 != 0:
        print("Es un año bisiesto")
    else:
        print("NO es un año bisiesto")
else:
    print("NO es un año bisiesto")

# Segunda opcion

if ano % 4 == 0 and ano % 100 != 0:
    print("Es un año bisiesto")
else:
    print("NO es un año bisiesto")
