#!usr/bin/python
# -*- coding: utf -8 -*-


"""
Función que recibe como parámetro una cadena de caracteres y devuelve la misma cadena invertida.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 27-02-2018
"""
palabra = raw_input("Introduzca una cadena de caracteres ")


def inversa(palabra):
    tam = len(palabra)
    pal_inv = []
    for i in range(tam-1):
        pal_inv = palabra[::-1] #Comando que invierte la cadena pasada
    print "La cadena invertida es ", pal_inv
    return pal_inv

inversa(palabra)
