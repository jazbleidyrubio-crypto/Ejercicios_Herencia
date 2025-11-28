# codigo_hija.py
from codigo_botella_menu import Botella

class Botella_contenido(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados, reciclable=True):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.reciclable = reciclable

    def compatibilidad_bebidas(self, tipo_bebida):
        if tipo_bebida.lower() in ["caliente", "fría"]:
            print(f"Compatible con bebidas {tipo_bebida}s.")
        else:
            print("Tipo de bebida no especificado correctamente.")

    def reutilizar(self):
        if self.reciclable:
            print("Esta botella puede reutilizarse varias veces ♻️")
        else:
            print("No es recomendable reutilizar esta botella.")

    def transparencia(self):
        print("El material permite ver el contenido interior con claridad.")
