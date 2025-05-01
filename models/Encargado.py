from Usuario import Usuario

class Encargado(Usuario):
    def __init__(self, idUsuario, nombreUsuario, password, nombre, apellido, email, idEncargado, disponible):
        super().__init__(idUsuario, nombreUsuario, password, nombre, apellido, email)
        self.__idEncargado = idEncargado
        self.__disponible = disponible