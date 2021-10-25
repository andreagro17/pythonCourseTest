from datetime import datetime

def preguntar_nombre_edad():
  nombre = input('¿Cómo te llamas?')
  print('Hola', nombre)
  edad = input(f'¿Cuántos años tienes {nombre}?')
  print(nombre, 'tienes', edad, 'anyos')
  resultado_vida = 100 - int(edad)
  
  today=datetime.now()
  year= 100-int(edad) + today.year
  return (f'¡Qué joven!, aún te quedan {resultado_vida} anyos hasta llegar a los 100 , en el año {year}.')

print(preguntar_nombre_edad())