'''
Ejercicio 1: Combustible

Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00.

'''
#Problema
# Calcular el rendimiento de combustible de un vehículo y el costo de un recorrido.

#Entradas
# distancia : real, distancia recorrida en kilómetros, mayor a 0.
# litros : real, cantidad de litros consumidos, mayor a 0.

#Salidas
# Distancia : real, kilómetros, formato de número con 2 decimales.
# Cantidad de litros : real, litros, formato de número con 2 decimales.
# Precio por litro : real, pesos mexicanos, formato de moneda con 2 decimales.
# Rendimiento : real, kilómetros por litro, formato de número con 2 decimales.
# Costo total del combustible consumido: real, pesos mexicanos, formato de moneda con 2 decimales.


#Reglas y supuestos
# - Cada litro de combustible tiene un costo fijo de $24.00.

#Algoritmo
# 1. Leer la distancia recorrida y la cantidad de litros consumidos.
# 2. Calcular el rendimiento: distancia / litros.
# 3. Calcular el costo: litros * 24.
# 4. Calcular el total a pagar: costo.
# 5. Mostrar la distancia recorrida, cantidad de litros consumidos, precio por litro, rendimiento y costo total del combustible consumido.

#Casos de prueba
# 120 km 10 L -> Distancia: 120.00 km, Cantidad de litros: 10.00 L, Precio por litro: 24.00, Rendimiento: 12.00 km/L, Costo total del combustible consumido: 240.00
# 250 km 20 L -> Distancia: 250.00 km, Cantidad de litros: 20.00 L, Precio por litro: 24.00, Rendimiento: 12.50 km/L, Costo total del combustible consumido: 480.00
# 180 km 15 L -> Distancia: 180.00 km, Cantidad de litros: 15.00 L, Precio por litro: 24.00, Rendimiento: 12.00 km/L, Costo total del combustible consumido: 360.00
# 300 km 25 L -> Distancia: 300.00 km, Cantidad de litros: 25.00 L, Precio por litro: 24.00, Rendimiento: 12.00 km/L, Costo total del combustible consumido: 600.00

# Contratos de funciones
# leerDatos() -> distancia, litros : leer y devolver la distancia recorrida y la cantidad de litros consumidos.
# calcularRendimiento(distancia, litros) -> rendimiento : calcular el rendimiento de combustible.
# calcularCosto(litros) -> costo : calcular el costo total del combustible consumido.
# mostrarResultados(distancia, litros, precio_litro, rendimiento, costo) -> None : mostrar la distancia recorrida, cantidad de litros consumidos, precio por litro, rendimiento y costo total del combustible consumido. Mostrar con Tabla mediante tabulate
def leerDatos():
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    litros = float(input("Ingrese la cantidad de litros consumidos: "))
    return distancia, litros

def calcularRendimiento(distancia, litros):
    rendimiento = distancia / litros
    return rendimiento

def calcularCosto(litros):
    precio_litro = 24.00
    costo = litros * precio_litro
    return costo

def mostrarResultados(distancia, litros, precio_litro, rendimiento, costo):
    from tabulate import tabulate
    headers = ["Distancia (km)", "Cantidad de litros (L)", "Precio por litro ($)", "Rendimiento (km/L)", "Costo total ($)"]
    data = [[f"{distancia:.2f}", f"{litros:.2f}", f"{precio_litro:.2f}", f"{rendimiento:.2f}", f"{costo:.2f}"]]
    print(tabulate(data, headers=headers, tablefmt="grid"))