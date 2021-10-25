import fnmatch
import os

## encuentra todos los archivos que empiezan por clase y con formato .py
patron = 'clase*.py'
print('Patrón :', patron)
print('*****')

ficheros = os.listdir('./')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))


########################################
patron = 'clase*.py'
print('Patrón :', patron)
print('*****')

ficheros = os.listdir('./')
# for nombre in ficheros:
#    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))
## FILTRA DENTRO DE LA LISTA Y DEVUELVE UN 'ARRAY' DE los ficheros que coinciden
print('Nombre: ', ficheros)
print('Coinciden: ', fnmatch.filter(ficheros, patron))