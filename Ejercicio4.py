'''Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.'''

from urllib import request

def numero_palabras_archivo_internet(url):
    f = request.urlopen(url)
    datos = f.read()
    palabras = datos.decode('utf-8').split()

    return len(palabras)

url1 = "https://www.gutenberg.org/files/2000/2000-0.txt"
url2 = "https://no-existe.txt"

print(numero_palabras_archivo_internet(url1))
print(numero_palabras_archivo_internet(url2))