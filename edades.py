#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro los nombres de personas, años de nacimiento y año en curso. La salida serán los nombres suministrados y la edad de cada una de las personas.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 02-03-2018
"""

n= int(raw_input("Cantidad de elementos a procesar "))
anio_curso= int(raw_input("Introduzca el año en curso "))
nombres= []
anios= []
i=0

for i in range(n):
    nom= raw_input("Introduzca el nombre de la persona ")
    nombres.append(nom)
    anno= int(raw_input("Introduzca el año de nacimiento "))
    anios.append(anno)

def calculoedad (nombres, anios, anio_curso, n):
    j=0
    edades= []
    for j in range(n):
        x= anio_curso-anios[j]
        edades.append(x)
    return edades

calculoedad (nombres, anios, anio_curso, n)
print "Nombres y edades respectivas"
print nombres, calculoedad (nombres, anios, anio_curso, n)
