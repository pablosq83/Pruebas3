#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro dos arreglos y se debe determinar si hay elementos en común o no. Devuelve cierto si hay al menos uno en común o de lo contrario devuelve falso.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 27-02-2018
"""

vector1 = []
n = int(input("Introduzca la cantidad de elementos a procesar de la lista "))
for i in range(n):
    elem = int(input("Introduzca un numero entero "))
    vector1.append(elem)

print"Segunda lista"

vector2 = []
m = int(input("Introduzca la cantidad de elementos a procesar de la 2 lista "))
for j in range(m):
    elem2 = int(input("Introduzca un numero entero "))
    vector2.append(elem2)

def superposicion(vector1, vector2):
    i=0
    j=0
    cont= 0
    cont2= 0
    for i in range(n):
        for j in range(m):
            if (vector1[i]==vector2[j]): #Compara ambas listas
                cont= cont+1
            else:
                cont2= cont2+1
    if (cont>0):
        valor= True
    else:
        valor= False
    return valor

if (superposicion(vector1, vector2)==True):
    print "Los arreglos tienen elementos en comun"
else:
    print "Los arreglos son distintos"
