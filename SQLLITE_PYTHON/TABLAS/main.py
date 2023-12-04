import orm
from  tablas.autores import autores
#autores
from  tablas.usuarios import usuarios
from  tablas.libros import libros

db=orm.SQLiteORM("db_biblioteca")
db.crear_tabla(autores)
db.crear_tabla(libros)
db.crear_tabla(usuarios)



#autor_uno_={
 #   "dni":7891111,"nombre":"quevedo","apellidos":"escojalosrios"
  #  }
#db.insertarUno("autores",autor_uno_)
usuarios_varios=[
    {
        "dni":"9486566",
        "nombre":"nadine",
        "apellidos":"atoccsa",
        "f_nacimiento":"06/04/05",
        "estado":"activo"
    },
    {
        "dni":"57975",
        "nombre":"feli",
        "apellidos":"accachachua",
        "f_nacimiento":"06/09/05",
        "estado":"activo"
    },
    {
        "dni":"54798764",
        "nombre":"orlando",
        "apellidos":"aaaa",
        "f_nacimiento":"06/06/065",
        "estado":"inactivo"
    },
    {
        "dni":"2147945",
        "nombre":"yadira",
        "apellidos":"a343",
        "f_nacimiento":"06/04/09",
        "estado":"activo"
    },
    {
        "dni":"232344",
        "nombre":"nad",
        "apellidos":"atoa",
        "f_nacimiento":"06/08/05",
        "estado":"activo"
    }]
#db.insertarVarios("usuarios",usuarios_varios)
#muestra una lista tuplas
#print(db.mostrar("usuarios"))
#muestra un objeto con sus campod y sus valores
#print(db.mostrar("usuarios",type="objetos"))
#tambien puedo filtrar informacion
#print(db.mostrar("usuarios",where="nombre LIKE 'nad%'",type="objeto"))

#print(db.mostrar("usuarios",where="dni =57975",type="objeto"))


db.actualizar("usuario",{"estado":"activo"},where="nombre='yadira")
db.actualizar("usuario",{"f_nacimiento":11/08/05},
where="dni=234245354")


dato_actualizar={"nombre":"nad","apellidos":"ya es salida"}
db.actualizar("usuarios",dato_actualizar,where="dni=2435453")


db.eliminar("usuarios",where="nombre='orlando'")
db.eliminar("usuarios",where="dni=9486566")

print(db.mostrar("usuario",type="objeto"))



]

db.insertarvarios("Usuarios",usuarios_varios)
