from models.Persona import Persona
from models.Conectar import Conectar

class PersonaDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_persona(self, rut, nombre, apellido, email):
        persona = Persona(rut, nombre, apellido, email)
        
        sql = '''
            INSERT INTO persona(rut, nombre, apellido, email)
            VALUES (%s, %s, %s, %s)
        '''
        valores = (persona.rut, persona.nombre, persona.apellido, persona.email)
        
        return self.__conn.ejecutar_sql(sql, valores)

    def listar_personas(self):
        sql = '''
            SELECT rut, nombre, apellido, email
            FROM persona
        '''
        return self.__conn.listar(sql)

    def modificar_persona(self, rut, nombre, apellido, email):
        sql = '''
            UPDATE persona
            SET nombre = %s, apellido = %s, email = %s
            WHERE rut = %s
        '''
        valores = (nombre, apellido, email, rut)
        return self.__conn.ejecutar_sql(sql, valores)

    def eliminar_persona(self, rut):
        sql = '''
            DELETE FROM persona
            WHERE rut = %s
        '''
        return self.__conn.ejecutar_sql(sql, (rut,))