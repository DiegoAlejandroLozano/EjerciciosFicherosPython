'''Escribir una función que pida un número entero entre 1 y 10, lea el 
fichero tabla-n.txt con la tabla de multiplicar de ese número, done n 
es el número introducido, y la muestre por pantalla. Si el fichero no 
existe debe mostrar un mensaje por pantalla informando de ello.'''

import os

def mostrar_tabla_multiplicar(num):
    fichero = "tabla-%d.txt" % (num)
    resultado = ""
    print("")

    if os.path.isfile(fichero):
        f = open(fichero, 'r')
        texto = f.read()
        print(texto)
        f.close
        resultado = "El fichero %s fue leido con éxito !!!" % fichero
    else:
        resultado = "El fichero %s no existe !!!" % fichero

    return resultado

numero = int(input("Ingrese un número del 1 al 10: "))
print(mostrar_tabla_multiplicar(numero))