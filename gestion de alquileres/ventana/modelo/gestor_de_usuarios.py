#Gestor de usuario:
class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, password):
        if user_id in self.users:
            return "El usuario ya existe. Por favor, elige otro ID."
        else:
            self.users[user_id] = User(user_id, password)
            return "Usuario registrado exitosamente."

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return "Usuario eliminado exitosamente."
        else:
            return "El usuario no existe."

    def login_user(self, user_id, password):
        if user_id in self.users:
            if self.users[user_id].password == password:
                return "Inicio de sesión exitoso."
            else:
                return "Contraseña incorrecta."
        else:
            return "El usuario no existe."


user_manager = UserManager()