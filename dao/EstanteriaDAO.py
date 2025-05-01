class EstanteriaDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_estanteria(self, capacidad):
        # Implementar lógica para insertar una nueva estantería en la base de datos
        pass

    def listar_estanterias(self):
        # Implementar lógica para listar todas las estanterías de la base de datos
        pass

    def modificar_capacidad_estanteria(self, id_estanteria, nueva_capacidad):
        # Implementar lógica para modificar la capacidad de una estantería existente
        pass

    def eliminar_estanteria(self, id_estanteria):
        # Implementar lógica para eliminar una estantería de la base de datos
        pass