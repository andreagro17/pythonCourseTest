from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes1.db', echo=True)
# crear sesion a la bbdd

Session = sessionmaker(bind=engine)

# una vez conectados mediante esta sesion creamos las instancias
session = Session()
# Crear los registros en la db

usuario = Estudiante('juan', 'Juan', 'Perez', 'Lopez', 'Complu')
session.add(usuario)
usuario = Estudiante('ana', 'Ana', 'Perez', 'Lopez', 'Complu')
session.add(usuario)
usuario = Estudiante('Laura', 'Laura', 'Perez', 'Lopez', 'Complu')
session.add(usuario)

#Agregar a la bbdd

session.commit()


