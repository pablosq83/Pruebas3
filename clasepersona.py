#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que define la clase persona.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 06-03-2018
"""
class Persona:
    def _init_(self, nombres="", apellidos="", cedula="", edad=0):
        self.nombres= nombres
        self.apellidos= apellidos
        self.cedula= cedula
        self.edad= edad
    def leer_datos(self):    
        self.nombres= raw_input("Introduzca los nombres: ")
        self.apellidos= raw_input("Introduzca los apellidos: ")
        self.cedula= raw_input("Introduzca la cedula de identidad: ")
        self.edad= int(raw_input("Introduzca la edad: "))
    def imprimir_datos(self):
        print "Datos completos de la clase persona "
        print "Nombres: ", self.nombres
        print "Apellidos: ", self.apellidos
        print "Cedula: ", self.cedula
        print "Edad: ", self.edad

p= Persona()

p.leer_datos()
p.imprimir_datos()
