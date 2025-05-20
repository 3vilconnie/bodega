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
            SELECT u.nombreUsuario, p.nombre, p.apellido, p.email, p.rut, e.habilitado
            FROM encargado AS e INNER JOIN persona AS p ON p.rut = e.rut
            INNER JOIN usuario as u ON u.idusuario = e.idusuario 
        '''
        if self.__conn.listar(sql) != None:
            for i, e in enumerate(self.__conn.listar(sql)):
                print(f"{i+1}. {e[0]} - {e[1]} {e[2]} - {e[3]} - {e[4]} - {'Habilitado' if e[5] else 'Deshabilitado'}")
            return self.__conn.listar(sql)
        else:
            print("no se encontraron encargados")
            return None

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
            SELECT u.nombreUsuario, p.nombre, p.apellido, p.rut, e.habilitado
            FROM encargado AS e INNER JOIN persona AS p ON p.rut = e.rut
            INNER JOIN usuario AS u ON e.idUsuario = u.idUsuario
            WHERE u.nombreUsuario = %s AND u.password = %s AND e.habilitado = True
        '''
        valores = (nombreUsuario, password)
        usuario = self.__conn.listarUno(sql, valores)
        if usuario != None:
            nombreusuario, nombre, apellido, rut, habilitado = usuario
            print(f"sesion iniciada con exito: Bienvenido {nombreUsuario}!")
            return Encargado(nombreusuario, password, nombre, apellido, None, rut, habilitado)
        
        return None
    
    def listar_personal(self, rut):
        sql = '''
            SELECT u.nombreUsuario, p.nombre, p.apellido, p.email, p.rut, c.habilitado
            FROM conserje AS c INNER JOIN persona AS p ON p.rut = c.rut
            INNER JOIN usuario as u ON u.idusuario = c.idusuario
            WHERE c.rutencargado = %s
        '''
        valores = (rut,)
        resultado = self.__conn.listar(sql, valores)
        if resultado != []:
            for i, e in enumerate(resultado):
                print(f"{i+1}. {e[0]} - {e[1]} {e[2]} - {e[3]} - {e[4]} - {'Habilitado' if e[5] else 'Deshabilitado'}")
            return resultado
        else:
            print("no se encontraron conserjes asociados")
            return None
    
    def desvincular_conserje(self, rut):
        sql = '''
            UPDATE conserje
            SET rutEncargado = NULL
            WHERE rut = %s
        '''
        if self.__conn.ejecutar_sql(sql, (rut,)):
            print("conserje desvinculado")
            return True
        else:
            print("error al desvincular conserje")
        return 
    
    def listar_solicitudes(self, rut):
        sql = '''
            SELECT s.idsolicitud, s.fecha, s.rutconserje, s.estado
            FROM solicitud AS s INNER JOIN conserje AS c ON s.rutconserje = c.rut
            WHERE c.rutEncargado = %s
        '''
        valores = (rut,)
        resultado = self.__conn.listar(sql, valores)
        if resultado != []:
            for i, e in enumerate(resultado):
                print(f"{i+1}. {e[0]} - {e[1]} {e[2]} - {e[3]}")
            return resultado
        else:
            print("no se encontraron solicitudes asociadas")
            return None