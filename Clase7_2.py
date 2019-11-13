# Objetos Todos los objetos tienen atributos (caracteristicas) y metodos (funcionalidades) Los objetos heredan
# caracteristicas Polimorfismo: Un objeto se puede comportar como 1 o mas objetos diferentes en distintos momentos en
# el tiempo, ya que comparten caracteristicas en comun
# Encapsulamiento de objetos: Definirlo para poder usarlo las veces que quiera y donde quiera
# Caracteristicas privadas y caracteristicas privadas

# import paquetes.carro as car
from paquetes import carro

micarro = carro.carro()
micarro.nEjes = 2
micarro.asignarTipo("Aereo")
print(micarro.devolverTipo(), micarro.nEjes)
