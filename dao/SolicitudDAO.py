from models.Conectar import Conectar
from models.Solicitud import Solicitud

class SolicitudDAO:
    def __init__(self):
        self.__conectar = Conectar()

    def insertar_solicitud(self, fecha, rutConserje):
        solicitud = Solicitud(fecha, rutConserje)
        sql = """
            INSERT INTO solicitud (fecha, rutConserje) 
            VALUES (%s, %s) 
        """
        valores = (solicitud.fecha, solicitud.rutConserje)
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Solicitud registrada exitosamente')
        else:
            print('No se pudo registrar la solicitud')

    def listar_solicitudes(self):
        sql = '''
            SELECT fecha, rutConserje
            FROM solicitud
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for solicitud in listado:
                print(f'Fecha: {solicitud[0]}, Conserje: {solicitud[1]}')

    def eliminar_solicitud(self, fecha):
        sql = '''
            DELETE FROM solicitud
            WHERE fecha = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (fecha,)):
            print('Solicitud eliminada exitosamente')
        else:
            print('No se encontró la solicitud')
    
    def agregarProducto(self):
        pass