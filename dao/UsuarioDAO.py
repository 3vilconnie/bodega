from models.Conectar import Conectar
from models.Usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.__conectar = Conectar()

    def insertar_usuario(self, nombre_usuario, password, nombre, apellido, email):
        usuario = Usuario(nombre_usuario, password, nombre, apellido, email)
        
        sql = """
            INSERT INTO usuario (nombre_usuario, password, nombre, apellido, email) 
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            usuario.nombreUsuario,
            usuario.password,
            usuario.nombre,
            usuario.apellido,
            usuario.email
        )
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el usuario en la base de datos')
        else:
            print('No se logró registrar el usuario')

    def listar_usuarios(self):
        sql = '''
            SELECT nombre_usuario, nombre, apellido, email
            FROM usuario
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for usuario in listado:
                print(f'Nombre de usuario: {usuario[0]}')
                print(f'Nombre: {usuario[1]}')
                print(f'Apellido: {usuario[2]}')
                print(f'Email: {usuario[3]}')
                print('------------------------------------')

    def modificar_usuario(self, nombre_usuario, nuevo_nombre, nuevo_apellido, nuevo_email):
        buscar_usuario = '''
            SELECT nombre_usuario
            FROM usuario
            WHERE nombre_usuario = %s
        '''
        usuario = self.__conectar.listarUno(buscar_usuario, (nombre_usuario,))
        if usuario:
            print('Usuario encontrado')
            modificar_usuario = '''
                UPDATE usuario
                SET nombre = %s, apellido = %s, email = %s
                WHERE nombre_usuario = %s
            '''
            if self.__conectar.ejecutar_sql(modificar_usuario, (nuevo_nombre, nuevo_apellido, nuevo_email, nombre_usuario)):
                print('Usuario modificado')
            else:
                print('No se pudo modificar el usuario')
        else:
            print('Usuario no existe')

    def eliminar_usuario(self, nombre_usuario):
        sql = '''
            DELETE FROM usuario
            WHERE nombre_usuario = %s              
        '''
        if self.__conectar.ejecutar_sql(sql, (nombre_usuario,)):
            print('Se eliminó el usuario')
        else:
            print('No se encontró el usuario')