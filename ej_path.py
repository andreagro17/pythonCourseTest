from pathlib import Path
import os
# me lo crea PATH.HOME en el escritorio...en el home de 'cada uno'
fichero_path = Path(Path.home(), 'directorio ficheros')
if not fichero_path.exists():
  os.mkdir(fichero_path)
  print('no existe')

fichero_path = fichero_path.joinpath('quijote2.txt')

with fichero_path.open('w') as file: 
  lineas = [
    'hola \n'
    'qie'

  ]
  file.writelines(lineas)