#!usr/bin/python
# -*- coding: utf -8 -*-

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
