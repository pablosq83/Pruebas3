#!usr/bin/python
# -*- coding: utf -8 -*-

palabra = raw_input("Introduzca una cadena de caracteres ")


def inversa(palabra):
    tam = len(palabra)
    pal_inv = []
    for i in range(tam-1):
        pal_inv = palabra[::-1]
    print "La cadena invertida es ", pal_inv
    return pal_inv

inversa(palabra)
