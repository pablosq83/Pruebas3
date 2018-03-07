#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Introducción a la POO - Herencia. Definición de la clase persona y la clase derivada estudiante. Uso de la instrucción import para obtener la clase base persona de otro archivo.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 07-03-2018
"""

from clasepersona import Persona

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

est = Estudiante()

print "Ingresar datos del estudiante "
# est.leer_datos()
est.leer_est()
#est.imprimir_datos()
est.imprimir_est()



