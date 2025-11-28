# clase padre

class Botella:
    def _init_(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    # ====== MÉTODOS ======
    def contener_liquidos(self):
        print("La botella puede contener líquidos de manera segura.")

    def facilitar_vertido(self):
        print("La forma de la botella facilita el vertido del líquido.")

    def cierre_hermetico(self):
        print("La tapa ofrece un cierre hermético.")

    def transporte(self):
        print("La botella es fácil de transportar.")

    def manejo(self):
        print("El diseño de la botella permite un buen manejo.")

    def compatibilidad_bebidas(self):
        print("Compatible con bebidas frías y calientes.")

    def reutilizacion(self):
        print("Esta botella es reutilizable dependiendo del material.")

    def transparencia(self):
        print("La transparencia depende del tipo de material.")
        
    def mostrar_info(self):
        print("===== INFORMACIÓN DE LA BOTELLA =====")
        print(f"Material     : {self.material}")
        print(f"Capacidad    : {self.capacidad} ml")
        print(f"Forma        : {self.forma}")
        print(f"Diseño       : {self.diseño}")
        print(f"Tapa         : {self.tapa}")
        print(f"Grabados     : {self.grabados}")