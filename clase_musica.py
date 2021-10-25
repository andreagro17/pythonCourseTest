class MusicFestival:
  def __init__(self, nombre, pais, estilo):
    self.nombre = nombre
    self.pais = pais
    self.estilo = estilo

# crear objeto con esa clase

festival1 = MusicFestival('MadCool', 'SP', 'Indi')

MusicFestival('BBK', 'SP', 'ROCK')
print(festival1.nombre)