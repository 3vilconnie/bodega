from Persona import Persona

class Usuario(Persona):
    def __init__(self, nombreUsuario, password, nombre, apellido, email, rut, idUsuario=None):
        super().__init__(rut, nombre, apellido, email)
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.password = password
        
    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, value):
        self._idUsuario = value

    @property
    def nombreUsuario(self):
        return self._nombreUsuario

    @nombreUsuario.setter
    def nombreUsuario(self, value):
        self._nombreUsuario = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value