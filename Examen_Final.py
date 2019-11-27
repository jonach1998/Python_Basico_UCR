annos = dict()
categorias = dict()
articulos = dict()
cat = dict()
art = dict()

with open("facturas-general.csv", "r") as documento:
    for line in documento:
        elementos = line.replace("\n", "").replace(",", ".").split(";")
        if int(elementos[7]) in annos.keys():
            annos[int(elementos[7])] += float(elementos[5])
            if elementos[6] in cat:
                categorias[int(elementos[7])][elementos[6]] += float(elementos[5])
            else:
                cat[elementos[6]] = float(elementos[5])
                categorias[int(elementos[7])] = cat
            if elementos[2] in art:
                articulos[int(elementos[7])][elementos[2]] += float(elementos[5])
            else:
                art[elementos[2]] = float(elementos[5])
                articulos[int(elementos[7])] = art
        else:
            annos[int(elementos[7])] = float(elementos[5])
            cat[elementos[6]] = float(elementos[5])
            categorias[int(elementos[7])] = cat
            art[elementos[2]] = float(elementos[5])
            articulos[int(elementos[7])] = art

with open("Informe 1", "w+") as informe1:
    for anno, venta in annos.items():
        informe1.write(f"{anno}: \n\tVentas: {venta: ,.3f} \n")

with open("Informe 2", "w+") as informe2:
    for anno, cadaDiccionario in categorias.items():
        informe2.write(f"{anno} \n")
        for categoria, venta in cat.items():
            informe2.write(f"\t{categoria} \n\t\tVentas: {venta: ,.3f} \n")

with open("Informe 3", "w+") as informe2:
    for anno, cadaDiccionario in articulos.items():
        informe2.write(f"{anno} \n")
        for producto, venta in art.items():
            informe2.write(f"\t{producto} \n\t\tVentas: {venta: ,.3f} \n")
