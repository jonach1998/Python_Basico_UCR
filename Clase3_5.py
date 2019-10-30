import codecs
archivo = open("leerme.txt", "r", encoding="iso-8859-1")
# for line in archivo:
#     linea = line.replace("\n", "")
#     print(line)

with open("resultado.txt", "w") as resultado:
    for line in archivo:
        line = line.replace("\n", " FL")
        print(line)
        resultado.write("%s\n" % line)
archivo.close()
