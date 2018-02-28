#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro una lista de palabras y devuelve la cadena mas larga.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 28-02-2018
"""

listap= []
n= int(raw_input("Tamaño de la lista de palabras "))
i=0

for i in range(n):
    aux= raw_input("Introduzca una palabra ")
    listap.append(aux)

def palabra_mas_larga (listap):
    tamanos= []
    j=0
    m= len(listap)
    for j in range(m):
        pal= listap[j]
        tamanos.append(len(pal))
    k=0
    mayor= tamanos[0]
    pos= 0
    for k in range(m):
        if (tamanos[k]>mayor):
            mayor= tamanos[k]
            pos= k
    palabralarga= listap[pos]
    return palabralarga

palabra_mas_larga(listap)
print"La palabra mas larga de la lista es ", palabra_mas_larga(listap)
