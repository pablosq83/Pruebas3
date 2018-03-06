#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que define la clase punto.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 06-03-2018
"""

class Punto:
    def _init_(self, x=0, y=0):
        self.x=x
        self.y=y
    def leer_datos(self):
        self.x= float(raw_input("Introduzca la abcisa "))
        self.y= float(raw_input("Introduzca la ordenada "))
    def imprimir_punto(self):
        print("Las coordenadas son "), self.x, self.y

p= Punto()

p.leer_datos()
p.imprimir_punto()
