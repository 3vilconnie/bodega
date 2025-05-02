from models.Conserje import Conserje
from models.Conectar import Conectar
from UsuarioDAO import UsuarioDAO

class ConserjeDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_conserje(self, nombreUsuario, password, nombre, apellido, email, rut):
        conserje = Conserje(nombreUsuario, password, nombre, apellido, email, rut)
        usuario = UsuarioDAO()
        if(usuario.insertar_usuario(conserje.nombreUsuario, conserje.password, conserje.nombre, conserje.apellido, conserje.email, conserje.rut)):
            print("usuario creado con exito.")
        
            sql = """
            INSERT INTO conserje (habilitado, rut, nombreUsuario) 
            VALUES (%s, %s, %s)
            """
            valores = (conserje.habilitado, conserje.rut, conserje.nombreUsuario)
        
            if self.__conectar.ejecutar_sql(sql, valores):
                print('Se ha registrado el conserje en la base de datos')
            else:
                print('No se logró registrar el conserje')
        else:
            print(f"error al crear usuario {conserje.nombreUsuario}")

    def listar_conserjes(self):
        sql = '''
            SELECT p.rut, p.nombre, p.apellido, p.email
            FROM conserje as c INNER JOIN persona AS p
            ON c.rut = p.rut 
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for conserje in listado:
                print(f'RUT: {conserje[0]}, Nombre: {conserje[1]}, Apellido: {conserje[2]}, Email: {conserje[3]}')

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
            SELECT p.nombre, p.apellido, u.nombreUsuario
            FROM conserje AS c INNER JOIN persona AS p ON c.rut = p.rut
            INNER JOIN usuario AS u ON c.idUsuario = u.idUsuario
            WHERE u.nombreUsuario = %s AND u.password = %s AND c.habilitado = True
        '''
        resultado = self.__conectar.listar(sql, (nombreUsuario, password))
        if resultado:
            print('Inicio de sesión exitoso')
            return True
        else:
            print('Credenciales incorrectas')
            return False
    