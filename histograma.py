#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro una lista de números enteros para generar un histograma.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 28-02-2018
"""

lista= []
i= 0
for i in range(3):
    aux= int(raw_input("Introduzca elemento de la lista "))
    lista.append(aux)

def histograma (lista):
    i=0
    j=0
    k=0
    for i in range(lista[0]):
        print "x",
    print "\n"
    for j in range(lista[1]):
        print "x",
    print "\n"
    for k in range(lista[2]):
        print "x",

histograma (lista)

