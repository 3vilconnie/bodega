from models.Conectar import Conectar
from models.Solicitud import Solicitud

class SolicitudDAO:
    def __init__(self):
        self.__conectar = Conectar()

    def insertar_solicitud(self, fecha, conserje):
        solicitud = Solicitud(fecha, conserje)
        sql = """
            INSERT INTO solicitud (fecha, conserje) 
            VALUES (%s, %s)
        """
        valores = (solicitud.fecha, solicitud.Conserje)
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Solicitud registrada exitosamente')
        else:
            print('No se pudo registrar la solicitud')

    def listar_solicitudes(self):
        sql = '''
            SELECT fecha, conserje
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