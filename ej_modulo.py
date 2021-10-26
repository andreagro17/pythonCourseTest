import os

print('antes de import')
import math

print('Antes funcion A')
def funcionA():
    print('FUNCION A')

print('Antes funcion B')
def funcionB():
    print('FUNCION B: {}'.format(math.sqrt(100)))

print('Antes del control __name__')
if __name__== '__main__':
  funcionA()
  funcionB()
print('Despues de control __name__')
      