#!usr/bin/python
# -*- coding: utf -8 -*-

"""
Programa que convierte un numero binario en decimal. Se asume que la entrada es válida.
Autor: Pablo Sulbarán (psulbaran@cenditel.gob.ve)
Fecha: 28-02-2018
"""

binario= int(raw_input("Introduzca un numero binario "))

decimal= 0
exp= 0

while (binario/10>0):
    digito= binario % 10
    print digito
    decimal= decimal + digito*(2**exp)
    exp= exp+1
    binario= binario/10

decimal = decimal + 2**exp # Se agrega este cálculo para tomar en cuenta el ultimo dígito que no entra en el lazo
print "Numero en sistema decimal es ",decimal


