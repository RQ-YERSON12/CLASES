import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios

# Suponiendo que tienes una base de datos SQLite llamada "db_biblioteca"
db = orm.SQLite("db_biblioteca")

# Crear tablas
db.crear_Tabla(Autores)
db.crear_Tabla(Libros)
db.crear_Tabla(Usuarios)

# Datos de ejemplo para un nuevo autor
# nuevo_autor = {
 #   "dni": "123456789",
  #  "nombre": "Nuevo",
   # "apellido": "Autor"
#}

# Insertar un registro en la tabla "Autores"
#db.insertaruno("Autores", nuevo_autor)
usuarios_varios=[
   
        {
            "id_usuario": 2 ,  
            "nombre": "sermon",
            "apellido": "texti",
            "correo": "rieras@gamil.com"
        }



]

db.insertarvarios("Usuarios",usuarios_varios)