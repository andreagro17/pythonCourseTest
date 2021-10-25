# Objetener los datos de ese fichero

# fichero = open("quijote_pg2000.txt", "r")
# for linea in fichero:
#   print(linea)
# # para no dejarlo en memoria 

# fichero.close()

# leer primeros caracteres
# dentro del argumento la cantidad de caracteres

# with open("quijote_pg2000.txt", "r") as fichero:
#   contenido = fichero.read(200)
#   print(contenido)

#lee la primera linea

# with open("quijote_pg2000.txt", "r") as fichero:
#   contenido = fichero.readline()
#   print(contenido)

#para leer párrafos de un fichero

with open("quijote_pg2000.txt", "r") as fichero:
  contenido = fichero.readlines(2000)
  print(contenido)
  # parrafo por parrado y los va acumulando hasta los 2000 caracteres
  for c in contenido:
    print(c.strip())
