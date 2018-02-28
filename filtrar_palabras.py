#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetros una lista de palabras y un entero, devolverá una lista de palabras cuya longitud sea mayor o igual al número entero pasado como parámetro. La función hará un filtrado de palabras de longitud n.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 28-02-2018
"""

listap= []
tam= int(raw_input("Tamaño de la lista de palabras "))
i=0

for i in range(tam):
    aux= raw_input("Introduzca una palabra ")
    listap.append(aux)

n= int(raw_input("Introduzca una longitud de palabras n "))

def filtrar (listap, n, tam): # Se añadió como parámetro el tamaño de la lista de palabras para reducir líneas de código
    palabrasgrandes= []
    i=0
    for i in range(tam):
        pal= listap[i]
        if (len(pal)>=n):
            palabrasgrandes.append(pal)
    return palabrasgrandes

filtrar (listap, n, tam)

print "\n"
print "Lista de palabras de longitud mayor a igual a n"
print "\n"
print filtrar(listap, n, tam)
        
