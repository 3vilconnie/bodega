from .Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombreUsuario, password, nombre, apellido, email, rut):
        super().__init__(nombreUsuario, password, nombre, apellido, email, rut)

    
        