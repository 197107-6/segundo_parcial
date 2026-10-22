'''
Ejercicio 1: Cine

Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. 

'''
#Problema
# Calcular el importe de una compra de boletos de cine considerando el precio por boleto, la cantidad de boletos y el descuento correspondiente.

#Entradas
# boletos : entero, cantidad de boletos, mayor o igual a 0.

#Salidas
# Cantidad de boletos: entero, cantidad de boletos, mayor o igual a 0.
# Precio por boleto: real, pesos mexicanos, formato de moneda con 2 decimales.
# Subtotal: real, pesos mexicanos, formato de moneda con 2 decimales.
# Descuento: real, pesos mexicanos, formato de moneda con 2 decimales.
# Total a pagar: real, pesos mexicanos, formato de moneda con 2 decimales.

#Reglas y supuestos
# - Cada boleto tiene un costo fijo de $75.00.
# - Si se compran 4 boletos o más, se aplica un descuento del 10% sobre el subtotal.
# - Si se compran menos de 4 boletos, no se aplica descuento.

#Algoritmo
# 1. Leer la cantidad de boletos.
# 2. Calcular el subtotal: boletos * 75.
# 3. Si boletos >= 4: aplicar descuento del 10%.
# 4. Si boletos < 4: no aplicar descuento.
# 5. Calcular el total a pagar: subtotal - descuento.
#6. Mostrar la cantidad de boletos, precio por boleto, subtotal, descuento y total a pagar.

#Casos de prueba
# 1 boletos -> Cantidad de boletos: 1, Precio por boleto: 75.00, Subtotal: 75.00, Descuento: 0.00, Total a pagar: 75.00
# 3 boletos -> Cantidad de boletos: 3, Precio por boleto: 75.00, Subtotal: 225.00, Descuento: 0.00, Total a pagar: 225.00
# 4 boletos -> Cantidad de boletos: 4, Precio por boleto: 75.00, Subtotal: 300.00, Descuento: 30.00, Total a pagar: 270.00
# 6 boletos -> Cantidad de boletos: 6, Precio por boleto: 75.00, Subtotal: 450.00, Descuento: 45.00, Total a pagar: 405.00

# Contratos de funciones
# leerCantidad() -> boletos : leer y devolver la cantidad de boletos.
# calcularSubtotal(boletos) -> subtotal : calcular el subtotal de la compra.
# calcularDescuento(subtotal, boletos) -> descuento : calcular el descuento aplicable.
# mostrarCompra(boletos, precio_boleto, subtotal, descuento, total) -> None : mostrar la cantidad de boletos, precio por boleto, subtotal, descuento y total a pagar. Mostrar con Tabla mediante tabulate

from tabulate import tabulate

def leerCantidad():
    boletos = int(input("Ingrese la cantidad de boletos: "))
    return boletos

def calcularSubtotal(boletos):
    precio_boleto = 75.00
    subtotal = boletos * precio_boleto
    return subtotal

def calcularDescuento(subtotal, boletos):
    if boletos >= 4:
        descuento = subtotal * 0.10
    else:
        descuento = 0.00
    return descuento

def mostrarCompra(boletos, precio_boleto, subtotal, descuento, total):
    from tabulate import tabulate
    headers = ["Cantidad de boletos", "Precio por boleto", "Subtotal", "Descuento", "Total a pagar"]
    data = [[boletos, f"${precio_boleto:.2f}", f"${subtotal:.2f}", f"${descuento:.2f}", f"${total:.2f}"]]
    print(tabulate(data, headers=headers, tablefmt="grid"))
