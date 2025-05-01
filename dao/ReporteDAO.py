from models.Conectar import Conectar
from models.Reporte import Reporte

class ReporteDAO:
    def __init__(self):
        self.__conectar = Conectar()

    def insertar_reporte(self, fecha):
        sql = """
            INSERT INTO reporte (fecha) 
            VALUES (%s)
        """
        valores = (fecha,)
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el reporte en la base de datos')
        else:
            print('No se logró registrar el reporte')

    def listar_reportes(self):
        sql = '''
            SELECT fecha
            FROM reporte
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for reporte in listado:
                print(f'Fecha del reporte: {reporte[0]}')

    def eliminar_reporte(self, fecha):
        sql = '''
            DELETE FROM reporte
            WHERE fecha = %s              
        '''
        if self.__conectar.ejecutar_sql(sql, (fecha,)):
            print('Se eliminó el reporte')
        else:
            print('No se encontró el reporte')