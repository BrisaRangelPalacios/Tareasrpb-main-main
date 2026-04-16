from models.UserModel import UsuarioModel
from models.schemas import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # Validar datos con el Schema
            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                email=email,
                password=password
            )

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "Error al crear usuario en la base de datos"

        except ValidationError as e:
            return False, e.errors()[0]['msg']