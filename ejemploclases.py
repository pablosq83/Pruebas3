#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que define una clase.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 06-03-2018
"""

class Persona:
    nombre= ""
    apellido= ""
    edad= 0

p = Persona()
p.nombre= "Pablo"
p.apellido= "Sulbaran"
p.edad= 35

print"Mi nombre es ",p.nombre, p.apellido, " y tengo ",p.edad
