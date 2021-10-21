# calcular la media de una serie de números
# *args pasa argumentos posicionales, busca argumentos que tiene y busca su posición.
# le paso argumentos posicionales al for para calcular la media de esos argumentos.

def calc_media(*args):
    total = 0
    for i in args:
      total += i
    resultado_media = total / len(args)
    return resultado_media

a, b, c, d = 1, 2, 3, 5
media = calc_media(a, b, c, d)

# Si ponemos un string (de text), las variables se ponen con {}
print(f'La media de {a}, {b} , {c} , {d} es: {media}')