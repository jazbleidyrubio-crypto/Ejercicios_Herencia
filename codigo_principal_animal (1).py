# llamar hijas y base de datos

from codigo_hija1_animal import terreste
from codigo_hija2_animal import acuatico
from base_de_datos_animales import base_datos_animales

# Crear instancia de la base de datos
bads = base_datos_animales()

## ====== Funciones para el funcionamiento del menu ======


def ingresar_animal():
    print("\n ingresar un nuevo animal")
    print("1. animal terrestre")
    print("2. animal acuático")
    tipo = input("seleccione el tipo de animal (1 o 2):")

    nombre = input("nombre: ")
    edad = input("edad: ")
    habitat = input("habitat: ")
    dieta = input("dieta: ")
    tamaño = input("tamaño: ")
    color = input("color: ")

    if tipo == "1":
        volar = input("volar: ")
        nuevo_animal = terreste(
            nombre,
            edad,
            habitat,
            dieta,
            tamaño,
            color,
            volar,
        )

    elif tipo == "2":
         respirar_branquias = input("respirar_branquias: ")
         nuevo_animal = acuatico(
            nombre,
            edad,
            habitat,
            dieta,
            tamaño,
            color,
            respirar_branquias,
        )
    else:
        print("opcion no valida.")
        return

    bads.ingresar_animal(nuevo_animal) 


def mostrar_animales():
    print("\n animales registrados: ")
    bads.mostrar_informacion()


def eliminar_animal():
    mostrar_animales()
    try:
        indice = int(input("\ningrese el numero del animal que desea eliminar: "))
        bads.eliminar_animal(indice)
    except ValueError:
        print(" por favor ingrese en numero valido.")


# menu principal


while True:
    print("\n=== menu principal ===")
    print("1. ingresar animal")
    print("2. mostrar animales")
    print("3.eliminar animal")
    print("4.salir")
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        ingresar_animal()
    elif opcion == "2":
        mostrar_animales()
    elif opcion == "3":
        eliminar_animal()
    elif opcion == "4":
        print("programa finalizado ")
        break
    else:
        print(" opcion no valida. intente de nuevo.")
