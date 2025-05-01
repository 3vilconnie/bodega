class OrdenCompra:
    def __init__(self, idCompra, idProducto, cantidad):
        self._idCompra = idCompra
        self._idProducto = idProducto
        self._cantidad = cantidad

    @property
    def idCompra(self):
        return self._idCompra

    @idCompra.setter
    def idCompra(self, value):
        self._idCompra = value

    @property
    def idProducto(self):
        return self._idProducto

    @idProducto.setter
    def idProducto(self, value):
        self._idProducto = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value
        