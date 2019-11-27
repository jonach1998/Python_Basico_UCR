annos = dict()
categorias = dict()
articulos = dict()
cat = dict()
art = dict()

with open("facturas-general.csv", "r") as documento:
    for line in documento:
        elementos = line.replace("\n", "").replace(",", ".").split(";")
        anno = int(elementos[7])
        venta = float(elementos[5])
        categoria = elementos[6]
        producto = elementos[2]
        if anno in annos.keys():
            annos[anno] += venta
            if categoria in cat:
                categorias[anno][categoria] += venta
            else:
                cat[categoria] = venta
                categorias[anno] = cat

            if producto in art:
                articulos[anno][producto] += venta
            else:
                art[producto] = venta
                articulos[anno] = art
        else:
            annos[anno] = venta
            cat[categoria] = venta
            categorias[anno] = cat
            art[producto] = venta
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
