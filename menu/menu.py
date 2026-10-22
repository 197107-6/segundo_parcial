from ejercicios import ejercicio1_cine as ej1
from ejercicios import ejercicio2_combustible as ej2

def mostrar_menu():
    print("Seleccione un ejercicio:")
    print("0. Salir")
    print("1. Ejercicio 1: Cine")
    print("2. Ejercicio 2: Combustible")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número del ejercicio que desea ejecutar: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            ej1.ejercicio1_cine()
        elif opcion == "2":
            ej2.ejercicio2_combustible()
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
    

def ejercicio1_cine():
    print("Ejercicio 1 pendiente")

def ejercicio2_combustible():
    print("Ejercicio 2 pendiente")