#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Se define una función que cuente la cantidad de cada una de las vocales de una palabra introducida, es decir cuente las "a", las "e", etc.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 02-03-2018
"""

palabra= raw_input("Introduzca una palabra ")

def vocales (palabra):
    conta=0
    conte=0
    conti=0
    conto=0
    contu=0
    contc=0
    for i in range(len(palabra)):
        if (palabra[i]=='a'):
            conta= conta+1
        elif (palabra[i]=='e'):
            conte= conte+1
        elif (palabra[i]=='i'):
            conti= conti+1
        elif (palabra[i]=='o'):
            conto= conto+1
        elif (palabra[i]=='u'):
            contu= contu+1
        else:
            contc= contc+1
    print "Cantidad de 'a' ",conta
    print "Cantidad de 'e' ",conte
    print "Cantidad de 'i' ",conti
    print "Cantidad de 'o' ",conto
    print "Cantidad de 'u' ",contu
    print "Cantidad de consonantes ", contc
    if ((contc>0) and (conta==0) and (conte==0) and (conti==0) and (conto==0) and (contu==0)) :
        print "La palabra solo tiene consonantes"

vocales (palabra)

