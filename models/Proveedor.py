from Usuario import Usuario

class Proveedor(Usuario):
    def __init__(self, productosDisponibles):
        self.productosDisponibles = productosDisponibles
        @property
        def productosDisponibles(self):
            return self._productosDisponibles

        @productosDisponibles.setter
        def productosDisponibles(self, value):
            self._productosDisponibles = value