'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes 
columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

1. Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
2. Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el 
mínimo, el máximo y la media de dada columna.'''

from os import path
import statistics

def modificar_cifras(cifra):

    nueva_cifra = ""

    if '.' in cifra:
        nueva_cifra = cifra.replace('.', '')
    else:
        nueva_cifra = cifra

    if ',' in nueva_cifra:
        nueva_cifra = nueva_cifra.replace(',', '.')

    return float(nueva_cifra)
    
    
def procesar_datos(nombre_fichero):

    dic_datos = {}
    nombre = []
    final = []
    máximo = []
    mínimo = []
    volumen = []
    efectivo = []

    if not path.isfile(nombre_fichero):
        #Si el fichero no existe, retorna None
        return None
    else:
        with open(nombre_fichero, 'r') as archivo:

            información = archivo.read().split('\n')
            
            for i in range(1, len(información)-1):
                datos = información[i].split(';')
                nombre.append(datos[0])
                final.append(modificar_cifras(datos[1]))
                máximo.append(modificar_cifras(datos[2]))
                mínimo.append(modificar_cifras(datos[3]))
                volumen.append(modificar_cifras(datos[4]))
                efectivo.append(modificar_cifras(datos[5]))

    dic_datos['nombres'] = nombre
    dic_datos['final'] = final
    dic_datos['máximo'] = máximo
    dic_datos['mínimo'] = mínimo
    dic_datos['volumen'] = volumen
    dic_datos['efectivo'] = efectivo

    return dic_datos

def archivo_csv(dic):
    with open("cotizacion_procesado.csv", 'w') as f:
        f.write("datos;valor máximo;valor mínimo;media\n")

        #Obteniendo las clases
        claves = dic.keys()

        for clave in claves:
            if clave != "nombres":
                datos = dic[clave]
                valor_máximo = max(datos)
                valor_mínimo = min(datos)
                media = statistics.mean(datos)

                f.write("%s;%.2f;%.2f;%.2f\n" % (clave, valor_máximo, valor_mínimo, media) )




diccionario_datos = procesar_datos("cotizacion.csv")
print(diccionario_datos.keys())
archivo_csv(diccionario_datos)