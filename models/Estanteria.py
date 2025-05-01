class Estanteria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value):
        self._capacidad = value