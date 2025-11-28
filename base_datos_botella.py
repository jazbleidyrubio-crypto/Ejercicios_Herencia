# base_datos.py
class BaseDatos:
    def __init__(self):
        self.lista_botellas = []

    def guardar_botella(self, nueva_botella):
        self.lista_botellas.append(nueva_botella)
        print("✅ Botella guardada con éxito.\n")

    def eliminar_botella(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            self.lista_botellas.pop(indice)
            print("🗑️ La botella fue eliminada correctamente.\n")
        else:
            print("❌ No se encontró una botella con ese número.\n")

    def mostrar_todas(self):
        if not self.lista_botellas:
            print("⚠️ No hay botellas registradas.\n")
            return

        for i, botella in enumerate(self.lista_botellas):
            print(f"\n🧾 Botella N° {i}")
            botella.mostrar_info()
