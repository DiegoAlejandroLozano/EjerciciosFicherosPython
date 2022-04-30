'''Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con 
la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero 
no existe debe mostrar un mensaje por pantalla informando de ello.'''

import os

def mostrar_tabla(n, m):
    nombre_fichero = "tabla-%d.txt" % n

    if os.path.isfile(nombre_fichero):
        fichero = open(nombre_fichero, 'r')
        lineas = fichero.readlines()
        print("La línea %d del fichero %s es: %s" % (m, nombre_fichero, lineas[m-1]))
        fichero.close()
    else:
        print("El fichero %s no existe :(" % nombre_fichero)

_n = int(input("Ingrese la tabla de multiplicar (del 1 al 10): "))
_m = int(input("Ingrese la línea que quiere ver (del 1 al 10): "))

mostrar_tabla(_n, _m)