# codigo_botella.py
class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    # Métodos generales
    def contener_liquidos(self):
        print(f"La botella 🍾 de {self.material} puede contener líquidos.")

    def facilitar_vertido(self):
        print("La forma de la botella facilita el vertido del líquido 💧.")

    def cierre_hermetico(self):
        if self.tapa:
            print("La botella tiene un cierre hermético gracias a su tapa 🍾.")
        else:
            print("La botella no posee tapa hermética 🍾.")

    def transportar(self):
        print("Es fácil de transportar por su ligereza y forma ergonómica.")

    def manejo(self):
        print("Se puede manejar fácilmente con una sola mano.")

    def mostrar_info(self):
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Forma: {self.forma}")
        print(f"Diseño: {self.diseño}")
        print(f"Tapa: {'Sí' if self.tapa else 'No'}")
        print(f"Grabados: {self.grabados}")
