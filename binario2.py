#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que recibe un número binario y lo convierte a decimal, se aplicarán algunas funciones ya establecidas en python.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 02-03-2018
"""

binario = int(raw_input("Introduzca un número binario "))

def numdecimal (binario):
    numbin= str(binario)
    decimal=0
    print numbin
    exp= len(numbin)-1
    for i in (numbin):
        decimal= decimal +(int(i)*(2**exp))
        exp= exp-1
    return decimal

numdecimal(binario)
print"El equivalente en sistema decimal es ",numdecimal(binario)

