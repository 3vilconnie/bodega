from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, listaEncargados):
        super()
        self.listaEncargados = listaEncargados
        
        @property
        def listaEncargados(self):
            return self._listaEncargados

        @listaEncargados
        def listaEncargados(self, value):
            self._listaEncargados = value