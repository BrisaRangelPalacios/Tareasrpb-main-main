from models.UserModel import UsuarioModel

class AuthController:

    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, password):
        return self.model.login(email, password)