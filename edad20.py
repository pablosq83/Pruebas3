#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Definir una tupla con las edades de 10 personas. Se deberá determinar cuantas personas tienen mas de 20 años.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha 02-03-2018
"""

edades= (20, 66, 33, 12, 18, 12, 65, 8, 45, 50)

def mayor20 (edades):
    cont=0
    for j in edades:
        if j>20:
            cont= cont+1
    return cont

mayor20(edades)
print "Personas con mas de 20 años ", mayor20(edades)
