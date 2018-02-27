#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Función que recibe como parámetro un caracter y determina si es vocal o cualquier otro tipo de caracter. Devuelve un valor lógico.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 27-02-2018
"""

caracter = raw_input("Introduzca un caracter ")

def letra(caracter):
    if ((caracter=='a')or(caracter=='e')or(caracter=='i')or(caracter=='o')or(caracter=='u')):
        return True
    else:
        return False

letra(caracter)

if (letra(caracter) == True):
    print "El caracter introducido es una vocal"
else:
    print "El caracter introducido es consonante, numero o caracter especial"
