# -*- 
# Bucles

# Repeticiones

grupo = ['Héctor', 'Foco', 'Carlos', 'Luis', 'Miguel']

# print(grupo[0])
# print(grupo[1])
# print(grupo[2])
# print(grupo[3])
# print(grupo[4])
# print(grupo[5])

# mi_tupla = (1,2)
i = 1  #  Acumulador
for nombre in grupo:
    print("El alumno en posición %s, se llama: %s" % (i, nombre))
    i += 1

# Factorial
# n! = n * (n - 1) ... * 1
# 4! = 4 * 3 * 2 * 1
# coleccion_4 = range(1, 5)

#. 4! = ( (4 * 3) * 2) * 1

x = 10
acumulador = 1
for n in range(1, x + 1):
    acumulador = acumulador * n

print(acumulador)


# Calcular el promedio de una lista
edades = [21, 34, 25, 34, 28, 23]
# Peromedio = suma de los datos / numero de datos

n = 0
for edad in edades:
    n += edad

longitudes = len(edades)
print(n/longitudes)
