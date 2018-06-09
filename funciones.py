# -*- coding: utf-8 -*-

# Funciones
# Conjunto de código que corre bajo demanda

def calcular_promedio(datos):
    suma = 0
    for dato in datos:
        suma += dato
    promedio = suma / len(datos)
    return promedio


# calcular_promedio([1, 2, 3])
# calcular_promedio([lista_edades)
# calcular_promedio([1, 2, 3, 334])
# calcular_promedio([1, 2, 3, 232])

def calcular_iva(precio, tasa_iva=1.16, imprimir=False):
    subtotal = precio / tasa_iva
    iva = precio - subtotal
    if imprimir:
        print(iva)
    return iva

# print(calcular_iva(100))
# print(calcular_iva(100, 1.25))
calcular_iva(200, 1.20)

# calcular_iva(116, True, 1.16)
calcular_iva(116, imprimir=True)

# *args
# **kwargs








