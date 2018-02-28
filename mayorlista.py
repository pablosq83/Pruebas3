#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que determina el mayor y menor elemento de una lista.
Autor: Pablo Sulbarán (psulbaran@cenditel.gov.ve)
Fecha: 27-02-2018
"""

lista= []
n= int(raw_input("Tamaño de la lista\n"))
i=0
for i in range(n):
    elem= int(raw_input("Introduzca un numero entero "))
    lista.append(elem)

def mayor (lista):
    may= lista[0]
    i=0
    for i in range(len(lista)):
        if (lista[i]>may):
            may= lista[i]
    return may

def menor (lista):
    men= lista[0]
    i=0
    for i in range(len(lista)):
        if (lista[i]<men):
            men= lista[i]
    return men

mayor(lista)
menor(lista)
print "El mayor elemento es ", mayor(lista)
print "El menor elemento es ", menor(lista)
