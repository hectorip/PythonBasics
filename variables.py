# -*- coding: utf-8 -*-
#
#
# Esto es un comentario

# ESto es un Here-doc

"""
Esto es el heredoc
"""

mensaje = '''
ESto también es un comentario o heredoc
Esto es otra línea
'''

# Cadenas de carácteres (strings)

nombre = "Héctor"
apellido = 'Patricio'  # Esta es la preferida

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)


print(len(nombre)) # length

# Función
print(nombre.upper())
print(nombre.lower())
print(nombre.replace('o', 'X'))


# Formateo de cadenas

mensaje_de_saludo = 'Hola soy %s, mucho gusto' % nombre
print(mensaje_de_saludo)

nombre_dado = input("Dime tu nombre: ")

# print("tu nombre tiene" + ' ' + len(nombre_dado) + ' ' + 'letras')
longitud_nombre = len(nombre_dado)

print("Tu nombre tiene: %s letras" % longitud_nombre)


print("Tu nombre tiene: %s letras" % len(nombre_dado + apellido))













