import mysql.connector
import datetime

database = mysql.connector.connect(

    host='localhost',
    user='root',
    passwd='',
    database='master_python',
    port=3306
)

# print(database)

# buffered muchas consultas con el cursor
cursor = database.cursor(buffered=True)


class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = 'INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)'
        usuario = (self.nombre, self.apellidos,
                   self.email, self.password, fecha)

        cursor.execute(sql, usuario)
        database.commit()
        return [cursor.rowcount, self]

    def identificar(self):
        pass
