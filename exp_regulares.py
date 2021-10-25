# import re
# # regex101.com
# texto = " Hoy es un dia magnifico y maravilloso"
# exp_reg = re.search("^Hoy.*oso$")

# #...

# # BIBLIOTECA GLOB PARA VER FICHEROS 

# import glob
# for fichero in glob.glob('ruta'):
#   print(fichero)

#   # en la consola : ' cat quijote1.txt '

entrada_agregar = """ en un lugar de la Mancha,,,,,,,"""

with open('quijote1.txt', 'a') as file:
  file.write(entrada_agregar)