'''Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la 
Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte 
por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.'''

from urllib import request

def pib_paises_unión_europea(pais):
    f = request.urlopen("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
    datos = f.read()
    tabla_datos_filas = datos.decode("utf-8").split("\n")

    
    años_pib = []       #Almacena todos los años disponibles
    valor_pib = []      #Almacena los valores PIB disponible
    
    #Guardando los años
    lista_años = tabla_datos_filas[0].split('\t')
    for año in range(1, len(lista_años)):
        años_pib.append(lista_años[año])

    #Recorriendo la tabla fila por fila, hasta encontrar la fila que contiene las iniciales
    for i in range(1, len(tabla_datos_filas)):
        iniciales = tabla_datos_filas[i].split("\t")[0].split(',')[2]
        
        #comparando las inciales encontradas, con la inicial requerida
        if iniciales == pais:
            pib_tabla = tabla_datos_filas[i].split('\t')            
            for i in range(1, len(pib_tabla)):
                valor_pib.append(pib_tabla[i])      

    #mostrando el PIB per cápita del país seleccionado durante todos los años disponibles
    for i in range(len(años_pib)):
        print("El PIB per cápita de %s durante el año %s fue: %s" % (pais, str(años_pib[i]), str(valor_pib[i])))

pais = input("Ingresa las iniciales de tu pais: ").upper()
pib_paises_unión_europea(pais)



