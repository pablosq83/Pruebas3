#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que cuenta las letras mayúsculas de una cadena introducida por teclado.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 28-02-2018
"""

cadena= raw_input("Introduzca una palabra ")
i=0
cont= 0

for i in range(len(cadena)):
    if (cadena[i].isupper()==1):
        cont= cont+1

if (cont>0):
    print cadena, " tiene ", cont," letras mayusculas"
else:
    print cadena," no tiene letras mayusculas"
