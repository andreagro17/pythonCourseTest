#verifica si es número primo

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equivale a', x, '*', n//x)
      break
    else:
      # el bucle sigue sin encontrar el factor
      print(n, 'es primo')