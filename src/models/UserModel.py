from models.databaseModel import Database
from datetime import datetime

class UsuarioModel:
    def __init__(self):
        self.db = Database().get_connection()
        self.cursor = self.db.cursor(dictionary=True)


    def validar_login(self, correo, password):
        query = "SELECT * FROM usuarios WHERE correo=%s AND password=%s"
        self.cursor.execute(query, (correo, password))
        user = self.cursor.fetchone()

        if user:
            self.actualizar_ingreso(user["id_usuario"])
        return user

    def registrar(self, nombre, apellido, correo, password, telefono, fecha):
        try:
            query = """
                INSERT INTO usuarios 
                (nombre, apellido, correo, password, telefono, fecha_registro)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nombre, apellido, correo, password, telefono, fecha))
            self.db.commit()

            return self.obtener_por_correo(correo), "Usuario registrado"
        except Exception as e:
            return None, f"Error: {str(e)}"

    def obtener_por_correo(self, correo):
        query = "SELECT * FROM usuarios WHERE correo=%s"
        self.cursor.execute(query, (correo,))
        return self.cursor.fetchone()

    def modificar(self, id_usuario, nombre, apellido, telefono):
        try:
            query = """
                UPDATE usuarios 
                SET nombre=%s, apellido=%s, telefono=%s
                WHERE id_usuario=%s
            """
            self.cursor.execute(query, (nombre, apellido, telefono, id_usuario))
            self.db.commit()
            return True
        except:
            return False

    def actualizar_ingreso(self, id_usuario):
        query = "UPDATE usuarios SET ultimo_ingreso=%s WHERE id_usuario=%s"
        self.cursor.execute(query, (datetime.now(), id_usuario))
        self.db.commit()

    
    def cerrar_sesion(self, id_usuario):
        self.actualizar_ingreso(id_usuario)