#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Se va a definir una función que de una lista de n palabras, contabilice cuántas comienzan por un caracter dado.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 02-03-2018
"""

n= int(raw_input("Introduzca el número de palabras "))
i=0
listap= []

for i in range(n):
    aux= raw_input("Introduzca una palabra ")
    listap.append(aux)

c= raw_input("Introduzca un caracter ")

def cuenta_palabra (listap, c, n):
    cont=0
    j=0
    for j in range(n):
        pal= listap[j]
        if pal[0]==c:
            cont= cont+1
    return cont

num= cuenta_palabra(listap, c, n)
print "El numero de palabras que comienzan por ",c," es ", num
