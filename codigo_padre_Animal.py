# Clase padre

class Animal:
    # Constructor de padre
    def __init__(self, nombre,edad,habitat,dieta,tamaño,color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print(f"{self.nombre} se esta moviendo")

    def comunicacion(self):
        print(f"{self.nombre} se esta comunicando")

    def reproducion(self):
        print(f"{self.nombre} a tenido desendancia")

    def alimentacion(self):
        print(f"{self.nombre} se esta alimentando ")

    def adaptacion(self):
        print(f"{self.nombre} se esta adaptando a los cambios ")

    def instintos(self):
        print(f"los instintos del {self.nombre} se activaron")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"habitat: {self.habitat}")
        print(f"dieta: {self.dieta}")
        print(f"tamaño: {self.tamaño}")
        print(f"Color: {self.color}")
