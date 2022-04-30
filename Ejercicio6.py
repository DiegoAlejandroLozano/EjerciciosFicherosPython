'''Escribir un programa para gestionar un listín telefónico con los nombres 
y los teléfonos de los clientes de una empresa. El programa incorporar funciones 
crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, 
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín 
debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su 
teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

from os import path
from unittest import result

def crear_archivo():
    '''Función encargada de crear el archivo si no existe'''

    if not path.isfile("listin.txt"):
        #Si el archivo no existe        
        archivo = open("listin.txt", 'w')
        encabezado = "Nombre,Telefono\n"
        archivo.write(encabezado)
        archivo.close()


def consultar_telefono(nombre_cliente):
    '''Función encargada de consultar el teléfono de un cliente'''

    archivo = open("listin.txt", 'r')
    contenido = archivo.readlines()
    archivo.close()
    telefono = ''

    for i in range(1, len(contenido)):
        nombre = contenido[i].split(',')[0]
        if nombre == nombre_cliente:
            return contenido[i].split(',')[1]
    
    return "El usuario %s no fue encontrado en la base de datos" % nombre_cliente
        

def añadir_nuevo_cliente(nombre, telefono):
    '''Función encargada de añadir un nuevo cliente con su teléfono'''

    archivo = open("listin.txt", 'a')
    nueva_linea = "%s,%s\n" % (nombre, telefono)
    archivo.write(nueva_linea)
    print("El usuario %s fue agregado con éxito" % nombre)
    archivo.close()

def eliminar_cliente(nombre_cliente):
    '''Función encargada de eliminar un cliente de la base de datos'''

    #Se debe leer el contenido del archivo
    archivo = open("listin.txt")
    contenido = archivo.readlines()
    archivo.close()
    resultado = ""

    #Procesando el contenido
    for i in range(1, len(contenido)):

        nombre_usuario = contenido[i].split(',')[0]

        if nombre_usuario == nombre_cliente:

            contenido.pop(i)
            #Luego de eliminar el cliente, se vuelve a sobre escribir el contenido en el archivo
            archivo = open("listin.txt", 'w')
            archivo.writelines(contenido)
            archivo.close()

            return "El usuario %s fue eliminado con éxito!!!" % nombre_cliente

    return "El usuario %s no fue encontrado en la base de datos" % nombre_cliente

def clientes():
    '''Función encargada de gestionar los clientes'''

    crear_archivo()

    continuar = "si"

    while continuar == "si":
        print("\nSeleccione la opción: ")
        print("1. Consultar teléfono\n2. Añadir cliente nuevo\n3. Eliminar cliente")
        respuesta = int(input("\n>>: "))
        
        if respuesta == 1:
            nombre = input("Ingrese el nombre del cliente: ").lower()
            print("El número del clientes es: %s" % consultar_telefono(nombre))
        elif respuesta == 2:
            nombre = input("Ingrese el nombre del cliente nuevo: ").lower()
            telefono = input("Ingrese el número del cliente: ")
            añadir_nuevo_cliente(nombre, telefono)
        elif respuesta == 3:
            nombre = input("Ingrese el nombre del cliente a eliminar: ").lower()
            print(eliminar_cliente(nombre))

        continuar = input("\nDesea continuar (si/no): ").lower()

#Iniciando la aplicación
clientes()




