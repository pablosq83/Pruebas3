#!usr/bin/python
# -*- coding: utf -8 -*-
#Primer programa en python

"""
Procedimiento que compara dos números reales y determina cual es el mayor
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 27-02-2018
"""

n1 = float(raw_input("Introduzca el primer numero "))
n2 = float(raw_input("Introduzca el segundo numero "))

def max2(n1, n2):
    if (n1>n2):
        print 'El mayor de los numeros es', n1
    elif (n2>n1):
        print 'El mayor de los numeros es', n2
    else:
        print 'Los numeros son iguales'

max2(n1,n2)


