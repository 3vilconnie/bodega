class Estanteria:
    def __init__(self, capacidad, idBodega=None):
        self.capacidad = capacidad
        self.idBodega = idBodega
    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value):
        self._capacidad = value
    @property
    def idBodega(self):
        return self._idBodega

    @idBodega.setter
    def idBodega(self, value):
        self._idBodega = value
