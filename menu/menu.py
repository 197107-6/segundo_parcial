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
            print("Ejecutando Ejercicio 1: Cine")
            ejercicio1_cine()
        elif opcion == "2":
            print("Ejecutando Ejercicio 2: Combustible")
            ejercicio2_combustible()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
    

def ejercicio1_cine():
    boletos = ej1.leerCantidad()
    subtotal = ej1.calcularSubtotal(boletos)
    descuento = ej1.calcularDescuento(subtotal, boletos)
    total = subtotal - descuento
    ej1.mostrarCompra(boletos, 75.00, subtotal, descuento, total)

def ejercicio2_combustible():
    distancia, litros = ej2.leerDatos()
    rendimiento = ej2.calcularRendimiento(distancia, litros)
    costo = ej2.calcularCosto(litros)
    precio_litro = 24.00
    ej2.mostrarResultados(distancia, litros, precio_litro, rendimiento, costo)
   