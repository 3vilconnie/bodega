from models.Administrador import Administrador
from models.Conectar import Conectar
from .UsuarioDAO import UsuarioDAO

class AdministradorDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_administrador(self, nombreUsuario, password, nombre, apellido, email, rut):
        administrador = Administrador(nombreUsuario, password, nombre, apellido, email, rut)
        usuario = UsuarioDAO()
        if usuario.insertar_usuario(administrador.nombreUsuario, administrador.password, administrador.nombre, administrador.apellido, administrador.email, administrador._rut):
            print("usuario creado con exito")
            sql = '''
            INSERT INTO administrador(idusuario, rut)
            VALUES (%s, %s)
            '''
            idusuario = usuario.obtener_id_usuario(administrador._rut)
            valores = (idusuario,  
                   administrador._rut)
        
            return self.__conn.ejecutar_sql(sql, valores)
        else:
            print("error al crear usuario.")

    def listar_administradores(self):
        sql = '''
            SELECT a.nombreUsuario, p.nombre, p.apellido, p.email
            FROM administrador AS a INNER JOIN persona AS p ON a.rut = p.rut
        '''
        return self.__conn.listar(sql)

    def modificar_administrador(self, idUsuario, nombreUsuario, password, nombre, apellido, email, rut):
        sql = '''
            UPDATE administrador as a
            INNER JOIN persona AS p ON a.rut = p.rut
            INNER JOIN usuario AS u ON a.nombreUsuario = u.nombreUsuario 
            SET u.nombreUsuario = %s, u.password = %s, p.nombre = %s, p.apellido = %s, p.email = %s
            WHERE a.rut = %s
        '''
        
        valores = (nombreUsuario, password, nombre, apellido, email, rut)
        return self.__conn.ejecutar_sql(sql, valores)

    def eliminar_administrador(self, rut):
        sql = '''
            DELETE FROM administrador
            WHERE rut = %s
        '''
        return self.__conn.ejecutar_sql(sql, (rut,))
    
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT nombreUsuario, nombre, apellido
            FROM administrador AS a INNER JOIN persona AS p ON p.rut = a.rut
            INNER JOIN usuario AS u ON a.idUsuario = u.idUsuario
            WHERE u.nombreUsuario = %s AND u.password = %s
        '''
        valores = (nombreUsuario, password)
        if self.__conn.listarUno(sql, valores) != None:
            print(f"sesion iniciada: Bienvenido {nombreUsuario}")  
            return True
        
        return False
    
    def habilitar_encargado(self, rut):
        sql = '''
            UPDATE encargado
            SET habilitado = true
            WHERE rut = %s
        '''
        if self.__conn.ejecutar_sql(sql, (rut,)):
            print("encargado habilitado")
            return True
        else:
            print("error al habilitar encargado")
            return False
    
    def deshabilitar_encargado(self, rut):
        sql = '''
            UPDATE encargado
            SET habilitado = false
            WHERE rut = %s
        '''
        return self.__conn.ejecutar_sql(sql, (rut,))