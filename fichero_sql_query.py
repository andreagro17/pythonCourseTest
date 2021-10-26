# para hacer consultas

from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes1.db', echo=True)

# Crea sesion
Session = sessionmaker(bind=engine)
session = Session()

#crea objetos

# for Estudiante in session.query(Estudiante).order_by(Estudiante.id):
#     print(Estudiante.nombre, Estudiante.apellido1, Estudiante.apellido2)

for Estudiante in session.query(Estudiante).filter(Estudiante.nombre == 'Juan'):
    print(Estudiante.nombre, Estudiante.apellido1, Estudiante.apellido2)