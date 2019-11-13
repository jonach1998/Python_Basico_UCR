# import paquetes.vehiculos as nose
from paquetes import vehiculos


class puerta:
    llavin = ""
    ventana = ""
    ventanaAbierta = False

    def abrirVentana(self):
        self.ventanaAbierta = True

    def cerrarVentana(self):
        self.ventanaAbierta = False


class carro(vehiculos.vehiculo):  # nose.vehiculo
    color = ""
    nPuertas = 0
    frenar = False
    velocidad = 0
    nEjes = 0
    lapuerta = puerta()

    def correr(self):
        if not self.frenar:
            self.velocidad += 1

    def detener(self):
        if self.velocidad == 0:
            self.frenar = True
        else:
            self.velocidad -= 1

    def asignarTipo(self, eltipo):
        self.__tipo = eltipo

    def devolverTipo(self):
        return self.__tipo
