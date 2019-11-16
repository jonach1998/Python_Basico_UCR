class Producto:
    nombreProducto = ""
    precio = 0
    unidad = ""

    def asignarNombre(self, nombre):
        self.nombreProducto = nombre

    def devolverNombre(self):
        return self.nombreProducto

    def asignarPrecio(self, precio):
        self.precio = precio

    def devolverPrecio(self):
        return self.precio

    def asignarUnidad(self, unidad):
        self.unidad = unidad

    def devolverUnidad(self):
        return self.unidad


class Ventas:
    nombreCliente = ""  # Nombre del cliente
    producto = ""  # Nombre del producto
    cantidadComprar = 0  # Cantidad a comprar
    montoVenta = 0.0  # Monto en que se va a vender
    tipoDescuento = ""  # El tipo de descuento que se va a aplicar
    montoVentaInicial = 0  # Monto en que se va a vender inicialmente (sin descuento)


class Distribuidor:
    descuento1 = 0.85  # Descuento de 15%, descuento cuando el monto de venta es mayor a 45_000
    descuento2 = 0.75  # Descuento de 25%, descuento cuando la cantidad es mayor a 650_000 litros

    listaProductos = dict()
    listaVentas = list()

    class resumen:
        tipoDescuento = ""
        monto = 0
        cantidadDescuento = 0

    # Este metodo se hace antes que los demas metodos,se hace cuando se crea el objeto
    def __init__(self):
        producto1 = Producto()
        producto1.asignarNombre("Cloro")
        producto1.asignarPrecio(10)
        producto1.asignarUnidad("Metro cubico")

        producto2 = Producto()
        producto2.asignarNombre("Algas")
        producto2.asignarPrecio(20)
        producto2.asignarUnidad("Metro cubico")

        producto3 = Producto()
        producto3.asignarNombre("Eliminacion de sedimentos")
        producto3.asignarPrecio(45)
        producto3.asignarUnidad("Metro cubico")

        # Se crea la lista de productos (literalmente), cada llave es el nombre del producto
        self.listaProductos = {producto1.nombreProducto: producto1, producto2.nombreProducto: producto2,
                               producto3.devolverNombre(): producto3}  # 2 Maneras de hacerlo, con la funcion o
        # accediendo directamente al atributo

    def ventaProducto(self, nombreCliente, nombreProducto, cantidad):
        ventaNueva = Ventas()
        ventaNueva.nombreCliente = nombreCliente
        ventaNueva.producto = nombreProducto
        ventaNueva.cantidadComprar = cantidad
        #  Se calcula la cantidad en metros cubicos, ya que se da en litros
        metroCubico = cantidad / 1000
        ventaNueva.montoVentaInicial = metroCubico * self.listaProductos[nombreProducto].devolverPrecio()  # Siempre es
        # mejor acceder a los atributos directamente, sin tener que usar metodos
        ventaNueva.montoVenta = ventaNueva.montoVentaInicial

        if 45_000 <= cantidad < 650_000:  # Descuento 1
            ventaNueva.montoVenta *= self.descuento1
            ventaNueva.tipoDescuento = "Descuento por monto"
        elif cantidad >= 650_000:  # Descuento 2
            ventaNueva.montoVenta *= self.descuento2
            ventaNueva.tipoDescuento = "Descuento por volumen"
        else:
            ventaNueva.tipoDescuento = "No tiene descuento"
        self.listaVentas.append(ventaNueva)

        return f"\nCliente: {ventaNueva.nombreCliente:} \nMonto inicial: {ventaNueva.montoVentaInicial:} \nTipo de " \
               f"descuento: {ventaNueva.tipoDescuento} \nMonto final: {ventaNueva.montoVenta:}"

    def devolverNombreProductos(self):
        return self.listaProductos.keys()

    def cierreCaja(self):
        cantidadVentas = len(self.listaVentas)
        cantidadTipo1 = 0
        cantidadTipo2 = 0
        cantidadTipoSinDescuento = 0
        montoTotalTipo1 = 0
        montoTotalTipo2 = 0
        montoTotalTipoSinDescuento = 0
        for cadaElementoLista in self.listaVentas:
            if cadaElementoLista.tipoDescuento == "Descuento por monto":
                cantidadTipo1 += 1
                montoTotalTipo1 += 0.15 * cadaElementoLista.montoVentaInicial
            elif cadaElementoLista.tipoDescuento == "Descuento por volumen":
                cantidadTipo2 += 1
                montoTotalTipo2 += 0.25 * cadaElementoLista.montoVentaInicial
            else:
                cantidadTipoSinDescuento += 1
                montoTotalTipoSinDescuento += cadaElementoLista.montoVentaInicial
        return f"\nMonto total de ventas sin descuento: {montoTotalTipoSinDescuento} \nMonto total de ventas con " \
               f"descuento por monto: {montoTotalTipo1} \nMonto total de ventas con descuento por volumen: " \
               f"{montoTotalTipo2} \nCantidad total de ventas: {cantidadVentas}"


while 1:
    miDistribuidora = Distribuidor()
    print("\nDistribuidor Jona \n")
    print("Que desea realizar")
    print("1. Venta")
    print("2. Cierre de caja")
    print("3. Salir")
    opcion = input("Seleccione la opcion: ")

    try:
        opcion = int(opcion)
    except ValueError:
        print("Favor digitar un valor numerico")
        continue

    if opcion == 3:
        break
    elif opcion == 1:
        cliente = input("\nDigite nombre del cliente: ")

        cantidad = int(input("Digite la cantidad de agua a tratar: "))

        for elemento in miDistribuidora.devolverNombreProductos():
            print(elemento)
        while 1:
            producto = input("\nDigite nombre del producto: ")
            try:
                print(miDistribuidora.ventaProducto(cliente, producto, cantidad))
                break
            except KeyError:
                print("Favor ingrese un producto valido")
    elif opcion == 2:
        print(miDistribuidora.cierreCaja())
        break
    else:
        print("Favor elegir una opcion valida")
