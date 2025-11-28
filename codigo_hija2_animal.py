from codigo_padre_Animal import Animal

# Clase hija PEZ
class acuatico(Animal):
    # Constructor de hija 2
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, respirar_branquias):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.respirar_branquias = respirar_branquias

    def comunicarse(self):
        return f"{self.nombre} se comunica mediante movimientos y burbujas."

    def moverse(self):
        return f"{self.nombre} se mueve nadando rápidamente."

    # MÉTODO EXTRA
    def respirar_branquias(self):
        return f"{self.nombre} está respirando con sus branquias."