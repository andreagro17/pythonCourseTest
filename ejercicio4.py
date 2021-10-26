import shutil, os
import pandas as pd

# crear variable origen donde pondré mi directorio principal
origen = './01001c.csv'
#si ponemos back sabemos que es un backup
destino = '/01001c.csv_bak'

#crear copia
shutil.copyfile(origen, destino)

#convertir a .tsv (opcion 'w' es escribir)
leer_csv = pd.read_csv('01001c.csv', sep=';')
with open('escribir_tsv.tsv', 'w', enconding='utf-8', newline='') as write_tsv:
  write_tsv(leer_csv.to_csv(sep='\t', index=False))
write_tsv.close()