from dao.Conectar import Conectar
from models.Estanteria import Estanteria

class EstanteriaDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_estanteria(self, capacidad, idBodega):
        estanteria = Estanteria(capacidad, idBodega)
        valores = (estanteria.idBodega, estanteria.capacidad)
        sql = '''
            INSERT INTO estanteria(idbodega, capacidad)
            VALUES (%s, %s)
        '''
        return self.__conectar.ejecutar_sql(sql, valores)
        
    def listar_estanterias(self):
        # Implementar lógica para listar todas las estanterías de la base de datos
        pass

    def modificar_capacidad_estanteria(self, id_estanteria, nueva_capacidad):
        # Implementar lógica para modificar la capacidad de una estantería existente
        pass

    def eliminar_estanteria(self, id_estanteria):
        # Implementar lógica para eliminar una estantería de la base de datos
        pass