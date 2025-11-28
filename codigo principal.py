# menu_principal.py
from codigo_hija_menu import Botella_contenido
from base_datos_botella import BaseDatos

# Crear base de datos
basd = BaseDatos()

def crear_botella():
    print("\n🧃 Crear nueva botella")
    material = input("Material: ")
    capacidad = input("Capacidad: ")
    forma = input("Forma: ")
    diseño = input("Diseño: ")
    tapa = input("¿Tiene tapa? (s/n): ").lower() == "s"
    grabados = input("Grabados o marca: ")
    reciclable = input("¿Es reciclable? (s/n): ").lower() == "s"

    nueva = Botella_contenido(material, capacidad, forma, diseño, tapa, grabados, reciclable)
    basd.guardar_botella(nueva)

def mostrar_botellas():
    basd.mostrar_todas()

def eliminar_botella():
    mostrar_botellas()
    try:
        indice = int(input("\nIngrese el número de la botella a eliminar: "))
        basd.eliminar_botella(indice)
    except ValueError:
        print("❌ Valor no válido.\n")

def mostrar_detalle():
    mostrar_botellas()
    try:
        indice = int(input("\nIngrese el número de la botella para ver detalles: "))
        if 0 <= indice < len(basd.lista_botellas):
            botella = basd.lista_botellas[indice]
            print("\n=== Detalle de la botella seleccionada ===")
            botella.mostrar_info()
            botella.contener_liquidos()
            botella.cierre_hermetico()
            botella.compatibilidad_bebidas("fría")
            botella.reutilizar()
        else:
            print("❌ Número fuera de rango.\n")
    except ValueError:
        print("❌ Valor no válido.\n")

def menu():
    while True:
        print("""
========= MENÚ DE BOTELLAS =========
1. Crear botella
2. Mostrar todas las botellas
3. Ver detalles de una botella
4. Eliminar botella
5. Salir
====================================
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_botella()
        elif opcion == "2":
            mostrar_botellas()
        elif opcion == "3":
            mostrar_detalle()
        elif opcion == "4":
            eliminar_botella()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida, intente nuevamente.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()
