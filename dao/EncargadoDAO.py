from models.Encargado import Encargado
from models.Conectar import Conectar
from .UsuarioDAO import UsuarioDAO

class EncargadoDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_encargado(self, nombreUsuario, password, nombre, apellido, email, rut, disponible=True):
        encargado = Encargado(nombreUsuario, password, nombre, apellido, email, rut, disponible)
        usuario = UsuarioDAO()
        
        if usuario.insertar_usuario(encargado.nombreUsuario, encargado.password, encargado.nombre, encargado.apellido, encargado.email, encargado._rut):
            print("usuario creado con exito.")
            
            sql = '''
                INSERT INTO encargado(rut, idusuario)
                VALUES (%s, %s)
            '''
            idusuario = usuario.obtener_id_usuario(encargado._rut)
            
            valores = (encargado._rut, idusuario)
            
            return self.__conn.ejecutar_sql(sql, valores)
        else:
            print("error al crear encargado")

    def listar_encargados(self):
        sql = '''
            SELECT u.nombreUsuario, p.nombre, p.apellido, p.email
            FROM encargado AS e INNER JOIN persona AS p ON p.rut = e.rut
            INNER JOIN usuario as u ON u.nombreUsuario = e.nombreUsuario 
        '''
        return self.__conn.listar(sql)

    def modificar_encargado(self, rut, password, nombre, apellido, email):
        sql = '''
            UPDATE conserje AS c
            INNER JOIN persona AS p ON c.rut = p.rut
            INNER JOIN usuario AS u ON c.nombreUsuario = u.nombreUsuario
            SET usuario.password = %s, persona.nombre = %s, persona.apellido = %s, email = %s
            WHERE p.rut = %s
        '''
        valores = (password, nombre, apellido, email, rut)
        return self.__conn.ejecutar_sql(sql, valores)

    def eliminar_encargado(self, rut):
        sql = '''
            DELETE FROM persona
            WHERE rut = %s
        '''
        return self.__conn.ejecutar_sql(sql, (rut,))
    
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT nombreUsuario, nombre, apellido
            FROM encargado AS e INNER JOIN persona AS p ON p.rut = e.rut
            INNER JOIN usuario AS u ON e.idUsuario = u.idUsuario
            WHERE u.nombreUsuario = %s AND u.password = %s AND u.habilitado = True
        '''
        valores = (nombreUsuario, password)
        if self.__conn.listarUno(sql, valores) != None:
            print(f"sesion iniciada con exito: Bienvenido {nombreUsuario}!")
            return True
        
        return False