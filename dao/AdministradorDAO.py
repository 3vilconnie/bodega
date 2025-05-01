from models.Administrador import Administrador
from models.Conectar import Conectar

class AdministradorDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_administrador(self, idUsuario, nombreUsuario, password, nombre, apellido, email, listaEncargados):
        administrador = Administrador(listaEncargados)
        administrador.idUsuario = idUsuario
        administrador.nombreUsuario = nombreUsuario
        administrador.password = password
        administrador.nombre = nombre
        administrador.apellido = apellido
        administrador.email = email
        
        sql = '''
            INSERT INTO administrador(idUsuario, nombreUsuario, password, nombre, apellido, email, listaEncargados)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        valores = (administrador.idUsuario, administrador.nombreUsuario, administrador.password, 
                   administrador.nombre, administrador.apellido, administrador.email, 
                   administrador.listaEncargados)
        
        return self.__conn.ejecutar_sql(sql, valores)

    def listar_administradores(self):
        sql = '''
            SELECT idUsuario, nombreUsuario, nombre, apellido, email, listaEncargados
            FROM administrador
        '''
        return self.__conn.listar(sql)

    def modificar_administrador(self, idUsuario, nombreUsuario, password, nombre, apellido, email, listaEncargados):
        sql = '''
            UPDATE administrador
            SET nombreUsuario = %s, password = %s, nombre = %s, apellido = %s, email = %s, listaEncargados = %s
            WHERE idUsuario = %s
        '''
        valores = (nombreUsuario, password, nombre, apellido, email, listaEncargados, idUsuario)
        return self.__conn.ejecutar_sql(sql, valores)

    def eliminar_administrador(self, idUsuario):
        sql = '''
            DELETE FROM administrador
            WHERE idUsuario = %s
        '''
        return self.__conn.ejecutar_sql(sql, (idUsuario,))
    
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT nombreUsuario, nombre, apellido
            FROM administrador as a INNER JOIN persona as p ON p.rut = a.rut
            INNER JOIN usuario as u ON a.idUsuario = u.idUsuario
            WHERE nombreUsuario = %s AND password = %s
        '''
        valores = (nombreUsuario, password)
        resultado = self.__conn.obtener_uno(sql, valores)
        
        return resultado