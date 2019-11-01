from time import time

t = time()
totalFemenino = 0
totalMasculino = 0
with open("PADRON_COMPLETO.txt", "r", encoding="iso-8859-1") as archlectura:
    for line in archlectura:
        elementos = line.split(",")
        sexo = int(elementos.pop(2))
        if sexo == 1:
            totalMasculino += 1
        elif sexo == 2:
            totalFemenino += 1
print("El total de mujeres es: ", totalFemenino)
print("El total de hombres es: ", totalMasculino)
print(totalMasculino+totalFemenino)

distritosDict = dict()
personasDistritos = dict()
with open("Distelec.txt", "r", encoding="iso-8859-1") as distritos:
    for line in distritos:
        elementos = line.replace("\n", "",).rstrip().split(",")
        cadaDistrito = int(elementos.pop(0))
        distritosDict[cadaDistrito] = elementos.pop()
        personasDistritos[cadaDistrito] = (0, 0)
with open("PADRON_COMPLETO.txt", "r", encoding="iso-8859-1") as archlectura:
    for line in archlectura:
        elementos = line.split(",")
        distrito = int(elementos.pop(1))
        sexo = int(elementos.pop(1))
        if sexo == 1:
            valorhombres = personasDistritos[distrito][0]
            valormujeres = personasDistritos[distrito][1]
            valorhombres += 1
            personasDistritos[distrito] = (valorhombres, valormujeres)
        elif sexo == 2:
            valorhombres = personasDistritos[distrito][0]
            valormujeres = personasDistritos[distrito][1]
            valormujeres += 1
            personasDistritos[distrito] = (valorhombres, valormujeres)
for numero, distrito in distritosDict.items():
    hombres = personasDistritos[numero][0]
    mujeres = personasDistritos[numero][1]
    print(f"En el distrito: {distrito} Mujeres: {mujeres} Hombres {hombres}")
print(time()-t)


