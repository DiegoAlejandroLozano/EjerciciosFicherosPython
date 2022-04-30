'''Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el 
nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.'''

def tabla_multiplicar(num):

    nombre_fichero = "tabla-%s.txt" % num    
    fichero = open(nombre_fichero, 'w')
    lineas = []

    for i in range(1, 11):
        linea = "%d X %d = %d\n" % (num, i, (i*num))
        lineas.append(linea)
    
    fichero.writelines(lineas)
    fichero.close()

    return "La tabla del %d fue creada en el fichero: %s" % (num, nombre_fichero)

numero = int(input("Ingrese un número del 1 al 10: "))
print(tabla_multiplicar(numero))

