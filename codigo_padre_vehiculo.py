#clase padre

class Vehiculo:
# constructor de padre 
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    # Métodos
    def arranque(self):
        print(f"El vehículo {self.modelo} está arrancando.")

    def apagado(self):
        print(f"El vehículo {self.modelo} se ha apagado.")

    def acelerar_frenar(self):
        print(f"El vehículo {self.modelo} está acelerando y frenando.")

    def sistema_direccion(self):
        print(f"El sistema de dirección del {self.modelo} está funcionando.")

    def climatizacion(self):
        print(f"El sistema de climatización del {self.modelo} está activo.")

    def tipo_seguridad(self):
        print(f"El vehículo {self.modelo} cuenta con sistemas de seguridad.")

    def luces(self):
        print(f"Las luces del vehículo {self.modelo} están encendidas.")

    def sistema_ventanas(self):
        print(f"Las ventanas del {self.modelo} están funcionando.")

    def sistema_espejo(self):
        print(f"El sistema de espejos del {self.modelo} está ajustándose.")

    def mostrar_info(self):
        print(f"\n--- Información del Vehículo ---")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Número de Puertas: {self.num_puertas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
