from models.Conserje import Conserje
from models.Conectar import Conectar

class ConserjeDAO:
    def __init__(self):
        self.__conectar = Conectar()  # Instancia objeto Conectar para ejecutar conexión a base de datos

    def insertar_conserje(self, rut, nombre, apellido, email):
        conserje = Conserje(rut, nombre, apellido, email)
        
        sql = """
            INSERT INTO conserje (rut, nombre, apellido, email) 
            VALUES (%s, %s, %s, %s)
        """
        valores = (conserje.rut, conserje.nombre, conserje.apellido, conserje.email)
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el conserje en la base de datos')
        else:
            print('No se logró registrar el conserje')

    def listar_conserjes(self):
        sql = '''
            SELECT rut, nombre, apellido, email
            FROM conserje
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for conserje in listado:
                print(f'RUT: {conserje[0]}, Nombre: {conserje[1]}, Apellido: {conserje[2]}, Email: {conserje[3]}')

    def modificar_conserje(self, rut, nombre, apellido, email):
        sql = '''
            UPDATE conserje
            SET nombre = %s, apellido = %s, email = %s
            WHERE rut = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (nombre, apellido, email, rut)):
            print('Conserje modificado')
        else:
            print('No se pudo modificar el conserje')

    def eliminar_conserje(self, rut):
        sql = '''
            DELETE FROM conserje
            WHERE rut = %s
        '''
        if self.__conectar.ejecutar_sql(sql, (rut,)):
            print('Conserje eliminado')
        else:
            print('No se encontró el conserje')
            
    def iniciar_sesion(self, nombreUsuario, password):
        sql = '''
            SELECT p.nombre, p.apellido, u.nombreUsuario
            FROM conserje as c INNER JOIN persona as p ON c.rut = p.rut
            INNER JOIN usuario as u ON c.idUsuario = u.idUsuario
            WHERE u.nombreUsuario = %s AND u.password = %s
        '''
        resultado = self.__conectar.listar(sql, (nombreUsuario, password))
        if resultado:
            print('Inicio de sesión exitoso')
            return True
        else:
            print('Credenciales incorrectas')
            return False
    