from models.Encargado import Encargado
from models.Conectar import Conectar
from PersonaDAO import PersonaDAO

class EncargadoDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_encargado(self, idUsuario, nombreUsuario, password, nombre, apellido, email, idEncargado, disponible=True):
        encargado = Encargado(idUsuario, nombreUsuario, password, nombre, apellido, email, idEncargado, disponible)
        person = PersonaDAO()
        
        if person.insertar_persona(encargado.rut, encargado.nombre, encargado.apellido, encargado.email):
            sql = '''
                INSERT INTO encargado(disponible, rut)
                VALUES (%s, %s)
            '''
            valores = (encargado.disponible, encargado.rut)
            
            return self.__conn.ejecutar_sql(sql, valores)
        else:
            print("error al crear encargado")

    def listar_encargados(self):
        sql = '''
            SELECT nombreUsuario, nombre, apellido, email
            FROM encargado AS e INNER JOIN persona AS p ON p.rut = e.rut
            INNER JOIN usuario as u ON u.idUsuario = e.idUsuario 
        '''
        return self.__conn.listar(sql)

    def modificar_encargado(self, idUsuario, nombreUsuario, password, nombre, apellido, email):
        sql = '''
            UPDATE encargado
            SET nombreUsuario = %s, password = %s, nombre = %s, apellido = %s, email = %s
            WHERE idUsuario = %s
        '''
        valores = (nombreUsuario, password, nombre, apellido, email, areaResponsabilidad, idUsuario)
        return self.__conn.ejecutar_sql(sql, valores)

    def eliminar_encargado(self, idUsuario):
        sql = '''
            DELETE FROM encargado
            WHERE idUsuario = %s
        '''
        return self.__conn.ejecutar_sql(sql, (idUsuario,))
    
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT nombreUsuario, nombre, apellido
            FROM encargado as e INNER JOIN persona as p ON p.rut = e.rut
            INNER JOIN usuario as u ON e.idUsuario = u.idUsuario
            WHERE nombreUsuario = %s AND password = %s
        '''
        valores = (nombreUsuario, password)
        resultado = self.__conn.obtener_uno(sql, valores)
        
        return resultado