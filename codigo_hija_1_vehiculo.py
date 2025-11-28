
from codigo_padre_vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, tipo_carroceria):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.tipo_carroceria = tipo_carroceria  # nuevo atributo

    def activar_radio(self):
        print(f"El carro {self.modelo} ha encendido la radio.")

    # Sobrescritura de método
    def arranque(self):
        print(f"El carro {self.modelo} arrancó suavemente (modo automóvil).")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carrocería: {self.tipo_carroceria}")
