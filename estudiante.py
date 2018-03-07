#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Introducción a la POO - Herencia. Definición de la clase persona y la clase derivada estudiante.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 07-03-2018
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

class Estudiante(Persona):
    def _init_(self, semestre = "", instituto = "", materias=0):
        self.instituto = instituto
        self.semestre = semestre
    def leer_est(self):
        self.instituto = raw_input("Introduzca el nombre de la institución donde estudia: ")
        self.semestre = raw_input("Introduzca el semestre en curso: ")
        self.materias = int(raw_input("Introduzca la cantidad de materias que cursa en este periodo lectivo: "))
    def imprimir_est(self):
        print "Datos del Estudiante"
        print "Institución: ", self.instituto
        print "Semestre: ", self.semestre
        print "Numero de materias cursando: ", self.materias

class Profesor(Persona):
    def _init_(self, mat_dictadas=0, area_interes = ""):
        self.mat_dictadas = mat_dictadas
        self.area_interes = area_interes
    def leer_prof(self):
        self.mat_dictadas = int(raw_input("Materias dictadas actualmente: "))
        self.area_interes = raw_input("Areas de investigación, extensión o interés: ")
    def imprimir_prof(self):
        print "Datos del profesor"
        print "Materias dictadas en este periodo: ", self.mat_dictadas
        print "Areas de investigación, interés o extensión: ", self.area_interes

est = Estudiante()
prof = Profesor()

print "Ingresar datos del estudiante "
est.leer_datos()
est.leer_est()
print "Ingresar datos del profesor "
prof.leer_datos()
prof.leer_prof()
est.imprimir_datos()
est.imprimir_est()
prof.imprimir_datos()
prof.imprimir_prof()

