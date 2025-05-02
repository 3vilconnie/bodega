from Usuario import Usuario

class Conserje(Usuario):
    def __init__(self, nombreUsuario, password, nombre, apellido, email, rut, idUsuario=None):
        super().__init__(nombreUsuario, password, nombre, apellido, email, rut, idUsuario)
        self._habilitado = False
        
    @property
    def habilitado(self):
        return self._habilitado

    @habilitado
    def habilitado(self, value):
        self._habilitado = value