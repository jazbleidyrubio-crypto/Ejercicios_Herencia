
class BaseDatosVehiculos:
    def __init__(self):
        self.lista_vehiculos = []

    def ingresar_vehiculo(self, nuevo_vehiculo):
        self.lista_vehiculos.append(nuevo_vehiculo)
        print("Vehículo ingresado con éxito")

    def eliminar_vehiculo(self, indice):
        if 0 <= indice < len(self.lista_vehiculos):
            self.lista_vehiculos.pop(indice)
            print("Vehículo eliminado correctamente")
        else:
            print("No se encontró un vehículo registrado con ese número")

    def mostrar_informacion(self):
        if not self.lista_vehiculos:
            print("No hay vehículos registrados")
            return

        for i, vehiculo in enumerate(self.lista_vehiculos):
            print(f"\nVehículo N° {i}")
            vehiculo.mostrar_info()
