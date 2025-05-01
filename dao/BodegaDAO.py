from models.Conectar import Conectar
from models.Bodega import Bodega

class BodegaDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_bodega(self, capacidad, encargado):
        bodega = Bodega(capacidad, encargado)
        
        sql = """
            INSERT INTO bodega (capacidad, encargado) 
            VALUES (%s, %s)
        """
        valores = (bodega.capacidad, bodega.encargado)
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado la bodega en la base de datos')
        else:
            print('No se logró registrar la bodega')

    def listar_bodegas(self):
        sql = '''
            SELECT capacidad, encargado
            FROM bodega
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for bodega in listado:
                print(f'Capacidad: {bodega[0]}')
                print(f'Encargado: {bodega[1]}')
                print('------------------------------------')

    def modificar_bodega(self, id_bodega, nueva_capacidad, nuevo_encargado):
        buscar_bodega = '''
            SELECT * 
            FROM bodega 
            WHERE id = %s
        '''
        bodega = self.__conectar.listarUno(buscar_bodega, (id_bodega,))
        if bodega:
            modificar_bodega = '''
                UPDATE bodega
                SET capacidad = %s, encargado = %s
                WHERE id = %s
            '''
            if self.__conectar.ejecutar_sql(modificar_bodega, (nueva_capacidad, nuevo_encargado, id_bodega)):
                print('Bodega modificada')
            else:
                print('No se pudo modificar la bodega')
        else:
            print('Bodega no existe')

    def eliminar_bodega(self, id_bodega):
        sql = '''
            DELETE FROM bodega
            WHERE id = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (id_bodega,)):
            print('Se eliminó la bodega')
        else:
            print('No se encontró la bodega')