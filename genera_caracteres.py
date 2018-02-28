#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro un entero y un caracter, el cual será impreso tantas veces según el parámetro pasado
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 27-02-2018
"""

c= raw_input("Introduzca un caracter ")
n= int(raw_input("Introduzca el numero de veces que se imprimirá el caracter suministrado "))

def genera_n_caracteres (c, n):
    i=0
    for i in range(n):
        print c,

genera_n_caracteres(c, n)
