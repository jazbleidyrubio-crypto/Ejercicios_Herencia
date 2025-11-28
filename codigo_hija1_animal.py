from codigo_padre_Animal import Animal

# Clase hija - PATO 
class terreste(Animal):
    # Constructor de hija 2
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, volar):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.volar = volar

    def comunicarse(self):
        return f"{self.nombre} dice 'cuac cuac'."

    def moverse(self):
        return f"{self.nombre} camina, vuela y nada."

    # Método extra
    def volar(self):
        return f"{self.nombre} está volando sobre el agua."