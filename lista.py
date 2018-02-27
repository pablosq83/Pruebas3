#!usr/bin/python
# -*- coding: utf -8 -*-

vector = []
n = int(input("Introduzca la cantidad de elementos a procesar de la lista "))
for i in range(n):
    elem = int(input("Introduzca un numero entero "))
    vector.append(elem)

suma = 0
prod = 1

for i in range(n):
    suma = suma + vector[i]
    prod = prod*vector[i]

print "La suma de los elementos del arreglo es ", suma
print "El producto de los elementos del arreglo es ", prod
    
    
