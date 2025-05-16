from .Usuario import Usuario

class Encargado(Usuario):
    def __init__(self, nombreUsuario, password, nombre, apellido, email, rut, disponible):
        super().__init__(nombreUsuario, password, nombre, apellido, email, rut)
        self.__disponible = disponible