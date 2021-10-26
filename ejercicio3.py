# Escribir un programa que tome una lista de números (entre 5 y 10 números) y
# haga una lista con el primero y el último de los elementos
# otra con el valor máximo y mínimo,
# y las muestre en pantalla.
import random

# x = list(range(1, 20, 2))
# print(x)

def listaAleatorios(n, m):
      lista = [0]  * 10
      for i in range(10):
          lista[i] = random.randint(n, m)
      max_value = max(lista)
      min_value = min(lista)
      return lista, (f'el máximo valor es: {max_value}, el min valor es: {min_value}, el ultimo elemento de la lista es:  {lista[-1]} , el primer elemento de la lista es: {lista[0]}')

print("Ingrese el primer número del rango de números con el que hacer una lista aleatoria ")
n=int(input())
print("Ingrese el segundo número del rango de números con el que hacer una lista aleatoria ")
m=int(input())

aleatorios=listaAleatorios(n,m)
print(aleatorios)

# def listaNum(a, b):
#     x = list(range(a,b))
#     print(x)

# print("Ingrese el rango de números con el que hacer una lista ")
# a=int(input())
# b=int(input())
# listaRango=listaNum(a,b)
# print(listaRango)