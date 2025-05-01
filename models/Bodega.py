class Bodega:
    def __init__(self, capacidad, encargado):
        self.capacidad = capacidad
        self.encargado = encargado
        
    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value):
        self._capacidad = value

    @property
    def encargado(self):
        return self._encargado

    @encargado.setter
    def encargado(self, value):
        self._encargado = value