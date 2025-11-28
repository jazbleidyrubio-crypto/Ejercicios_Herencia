
from codigo_padre_vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga = capacidad_carga  # nuevo atributo

    def cargar(self, peso):
        if peso <= self.capacidad_carga:
            print(f"El camión {self.modelo} ha cargado {peso} kg.")
        else:
            print(f"El peso excede la capacidad del camión {self.modelo}.")

    # Sobrescritura de método
    def arranque(self):
        print(f"El camión {self.modelo} arrancó con fuerza (modo carga pesada).")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de Carga: {self.capacidad_carga} kg")
