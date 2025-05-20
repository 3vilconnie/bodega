from models.Conserje import Conserje
from models.Conectar import Conectar
from .UsuarioDAO import UsuarioDAO

class ConserjeDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_conserje(self, nombreUsuario, password, nombre, apellido, email, rut):
        conserje = Conserje(nombreUsuario, password, nombre, apellido, email, rut)
        usuario = UsuarioDAO()
        if(usuario.insertar_usuario(conserje.nombreUsuario, conserje.password, conserje.nombre, conserje.apellido, conserje.email, conserje._rut)):
            print("usuario creado con exito.")
        
            sql = """
            INSERT INTO conserje (idusuario, rut, habilitado) 
            VALUES (%s, %s, %s)
            """
            idusuario = usuario.obtener_id_usuario(conserje._rut)
            valores = (idusuario, conserje._rut, conserje.habilitado)
        
            if self.__conectar.ejecutar_sql(sql, valores):
                print('Se ha registrado el conserje en la base de datos')
            else:
                print('No se logró registrar el conserje')
        else:
            print(f"error al crear usuario {conserje.nombreUsuario}")

    def listar_conserjes(self):
        sql = '''
            SELECT p.rut, p.nombre, p.apellido, p.email, c.habilitado, c.rutEncargado
            FROM conserje as c INNER JOIN persona AS p
            ON c.rut = p.rut
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for i, c in enumerate(listado):
                print(f"{i+1}. {c[0]} - {c[1]} {c[2]} - {c[3]} - {'Habilitado' if c[4] else 'Deshabilitado'} - {c[5] if c[5] != None else 'Sin Encargado'}")
            return listado
        else:
            print("No se encontraron conserjes")
            return None
    
    def listar_conserjes_sin_asignar(self):
        sql = '''
            SELECT p.rut, p.nombre, p.apellido, p.email, c.habilitado, c.rutEncargado
            FROM conserje as c INNER JOIN persona AS p
            ON c.rut = p.rut
            WHERE c.rutEncargado IS NULL
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for i, c in enumerate(listado):
                print(f"{i+1}. {c[0]} - {c[1]} {c[2]} - {c[3]} - {'Habilitado' if c[4] else 'Deshabilitado'} - {c[5] if c[5] != None else 'Sin Encargado'}")
            return listado
        else:
            print("No se encontraron conserjes disponibles")
            return None
    
    def modificar_conserje(self, rut, nombre, apellido, email):
        sql = '''
            UPDATE persona
            SET nombre = %s, apellido = %s, email = %s
            WHERE rut = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (nombre, apellido, email, rut)):
            print('Conserje modificado')
        else:
            print('No se pudo modificar el conserje')

    def eliminar_conserje(self, rut):
        sql = '''
            DELETE FROM persona
            WHERE rut = %s
        '''
        if self.__conectar.listarUno(sql, (rut, ) == 1):
            self.__conectar.ejecutar_sql(sql, (rut,))
            print('Conserje eliminado')
        else:
            print('No se encontró el conserje')
            
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT p.nombre, p.apellido, u.nombreUsuario, p.rut
            FROM conserje AS c INNER JOIN persona AS p ON c.rut = p.rut
            INNER JOIN usuario AS u ON c.idUsuario = u.idUsuario
            WHERE u.nombreusuario = %s AND u.password = %s AND c.habilitado = true
        '''

        print(f"Iniciando sesión... {nombreUsuario}")

        if self.__conectar.listarUno(sql, (nombreUsuario, password)) != None:
            print(f'Inicio de sesión exitoso: Bienvenido {nombreUsuario}')
            nombre, apellido, nombreUsuario, rut = self.__conectar.listarUno(sql, (nombreUsuario, password))
            conserje = Conserje(nombreUsuario, None, nombre, apellido, None, rut)
            return conserje
        
        print('Error: Usuario o contraseña incorrectos')
        return None
        
    def listar_solicitudes(self, rut):
        sql = '''
            SELECT s.idSolicitud, s.fecha, s.estado, 
            (SELECT COUNT(*) FROM solicitud AS s1 
            INNER JOIN lineaproducto AS l1 ON s1.idsolicitud = l1.sol_idsolicitud 
            INNER JOIN producto AS p ON p.idproducto = l1.pro_idproducto 
            WHERE s1.rutconserje = %s) AS total
            FROM solicitud AS s INNER JOIN conserje AS c ON s.rutConserje = c.rut
            WHERE s.rutconserje = %s
        '''
        listado = self.__conectar.listar(sql, (rut, rut))

        if listado is not None:
            for solicitud in listado:
                print(f'ID: {solicitud[0]}, Fecha: {solicitud[1]}, Estado: {solicitud[2]}, Total Productos: {solicitud[3]}')
        else:
            print('No hay solicitudes registradas')
    def id_ultima_solicitud(self, rut):
        sql = '''
            SELECT MAX(idSolicitud)
            FROM solicitud
            WHERE rutConserje = %s
        '''
        idSolicitud = self.__conectar.listarUno(sql, (rut,))
        if idSolicitud is not None:
            return idSolicitud[0]
        else:
            print('No se encontró la solicitud')
            return None
    
    def asignar_encargado(self, rutConserje, rutEncargado):
        sql = '''
            UPDATE conserje
            SET rutEncargado = %s
            WHERE rut = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (rutEncargado, rutConserje)):
            print('Encargado asignado al conserje')
        else:
            print('No se pudo asignar el encargado al conserje')