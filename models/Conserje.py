from Usuario import Usuario

class Conserje(Usuario):
    def __init__(self, rut, nombre, apellido, email):
        self._habilitado = False
        
    @property
    def habilitado(self):
        return self._habilitado

    @habilitado.setter
    def habilitado(self, value):
        self._habilitado = value