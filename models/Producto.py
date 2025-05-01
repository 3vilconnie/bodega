# Aplicar validacion de codigo
class Producto:
    # constructor
    def __init__(self, idProducto, nombreProducto, stock, stockCritico, disponible):
        # Atributos
        self.__idProducto = idProducto
        self.__nombreProducto = nombreProducto
        self.__stock = stock
        self.__stockCritico = stockCritico
        self.__disponible = disponible
        
    # Propiedad getter
    @property
    def nombreProducto(self):
        return self.__nombreProducto

    @nombreProducto.setter
    def nombreProducto(self, value):
        self.__nombreProducto = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    @property
    def stockCritico(self):
        return self.__stockCritico

    @stockCritico.setter
    def stockCritico(self, value):
        self.__stockCritico = value

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, value):
        self.__disponible = value