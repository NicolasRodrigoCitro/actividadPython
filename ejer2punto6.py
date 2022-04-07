frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
from collections import Counter
'''texto=frase.lower().split()
print(texto)
texto tiene una lista con con las palabras separadas pero repetidas- no me sirve'''

'''con Coubnter tengo un diccionario al cual paso a minusculas con lower y separo en palabras con split,
 y cada palabra tiene la cantidad de repeticiones en frase'''
c=Counter(frase.lower().split())
print(c)
print(" salto de linea\n")
#con Keys devuelvo una lista pero solo con las claves del diccionario
lista=[]
lista= c.keys()
print(lista)