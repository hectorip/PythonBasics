# -*- coding: utf-8 -*-

# Argumentos


def suma(otro, *args):
    print(type(args))

suma(1, 2, 3, 5, 5, 6, 7, 6, 7, 7)

def crear_persona(nombre, *args,**kwargs):
    print(kwargs)

crear_persona(9, nombre="hector", edad=28, pelo="negro")

