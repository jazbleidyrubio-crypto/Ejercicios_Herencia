from codigo_hija_1_vehiculo import Carro
from codigo_hija_2_vehiculo import Camion
from base_datos_vehiculos import BaseDatosVehiculos


# Crear instancia de la base de datos
bd = BaseDatosVehiculos()


# ====== Funciones del menú ======
def ingresar_vehiculo():
    print("\nIngresar un nuevo vehículo")
    print("1. Carro")
    print("2. Camión")
    tipo = input("Seleccione el tipo de vehículo (1 o 2): ")

    modelo = input("Modelo: ")
    color = input("Color: ")
    motor = input("Motor: ")
    num_puertas = input("Número de puertas: ")
    capacidad_pasajeros = input("Capacidad de pasajeros: ")
    tipo_combustible = input("Tipo de combustible: ")

    if tipo == "1":
        tipo_carroceria = input("Tipo de carrocería: ")
        nuevo_vehiculo = Carro(
            modelo,
            color,
            motor,
            num_puertas,
            capacidad_pasajeros,
            tipo_combustible,
            tipo_carroceria,
        )
    elif tipo == "2":
        capacidad_carga = int(input("Capacidad de carga (kg): "))
        nuevo_vehiculo = Camion(
            modelo,
            color,
            motor,
            num_puertas,
            capacidad_pasajeros,
            tipo_combustible,
            capacidad_carga,
        )
    else:
        print("Opción no válida.")
        return

    bd.ingresar_vehiculo(nuevo_vehiculo)


def mostrar_vehiculos():
    print("\nVehículos registrados:")
    bd.mostrar_informacion()


def eliminar_vehiculo():
    mostrar_vehiculos()
    try:
        indice = int(input("\nIngrese el número del vehículo que desea eliminar: "))
        bd.eliminar_vehiculo(indice)
    except ValueError:
        print("Por favor, ingrese un número válido.")


# ====== Menú principal ======
while True:
    print("\n=== Menú Principal ===")
    print("1. Ingresar vehículo")
    print("2. Mostrar vehículos")
    print("3. Eliminar vehículo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_vehiculo()
    elif opcion == "2":
        mostrar_vehiculos()
    elif opcion == "3":
        eliminar_vehiculo()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
