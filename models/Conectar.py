import mysql.connector # Importando mysql.connector

# Investigar try except con mysql.connector.error
# Aplicar try - except a clase conectar
# Apicar cerrar conexion a proyecto. self.__conn.close()
class Conectar:
    # Constructor
    def __init__(self):
        # Manejo de errores sera para mas adelante
        # Metodo connect de mysql.connector
        self.__conn = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = '',
            database = 'tienda'
        )
        self.__cursor = self.__conn.cursor() # Crea el cursor de la bd
        
    def ejecutar_sql(self, sql, valores): # INSERT, UPDATE, DELETE
        self.__cursor.execute(sql, valores) # Se encarga de ejecutars sql
        self.__conn.commit() # CONFIRMA CAMBIOS EN BASE DE DATOS
        if self.__cursor.rowcount > 0:
            return True
        return 

    def listar(self, sql): # SELECT
        self.__cursor.execute(sql) # Se encarga de ejecutar sql
        resultado = self.__cursor.fetchall() # [ (codigo, nombre, precio, stock), (codigo, nombre, precio, stock)]
        return resultado
    
    def listarUno(self, sql, value): # SELECT
        self.__cursor.execute(sql, value) # Se encarga de ejecutar sql
        resultado = self.__cursor.fetchone() # (codigo, nombre, precio, stock)
        return resultado
