from models.Conectar import Conectar
from models.Producto import Producto # Importa clase Conectar dentro de ProductoDAO

class ProductoDAO:
    def __init__(self):
        self.__conectar = Conectar() # Instancia objeto Conectar para ejecutar conexion a base de datos
        
    def insertar_producto(self, codigo, nombre, precio, stock):
        # Instanciar Producto
        producto = Producto(codigo, nombre, precio, stock)
        
        # Utilizando SQL para insertar nuevos datos
        sql = """
            INSERT INTO producto (codigo, nombre, precio, stock) 
            VALUES (%s, %s, %s, %s)
            """
        # Crear tupla de datos con objeto producto
        valores = (
            producto.codigo,
            producto.nombre,
            producto.precio,
            producto.stock
        )
        
        # Ejecutando sentencia sql DEVUELVE TRUE o FALSE
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el producto en la base de datos')
        else:
            print('No se logro registrar el producto')
            
    def listar_productos(self):
        sql = '''
            SELECT codigo, nombre, precio, stock
            FROM producto
            '''
        listado = self.__conectar.listar(sql) # [(codigo, nombre, precio, stock), (, , , )]
        if listado is not None:      #                0       1       2      3
            for producto in listado: # producto -> (codigo, nombre, precio, stock)
                print(f'Codigo producto: {producto[0]}')
                print(f'Codigo Nombre: {producto[1]}')
                print(f'Codigo Precio: {producto[2]}')
                print(f'Codigo Stock: {producto[3]}')
                print('------------------------------------')
        
    def modificar_nombre_producto(self, codigo, nombre):
        buscar_producto = '''
                        SELECT nombre
                        FROM producto
                        WHERE codigo = %s
                        '''
        producto = self.__conectar.listarUno(buscar_producto, (codigo, )) # (, , ,)
        if producto:
            print('Producto encontrado')
            modificar_producto = '''
                                UPDATE producto
                                SET nombre = %s
                                WHERE codigo = %s
                                '''
            if self.__conectar.ejecutar_sql(modificar_producto, (nombre, codigo)):
                print('Producto modificado')
            else:
                print('Producto no se pudo modificar')
        else:
            print('Producto no existe')
            
    def eliminar_producto(self, codigo):
        sql = '''
                DELETE FROM producto
                WHERE codigo = %s              
                '''
        if self.__conectar.ejecutar_sql(sql, (codigo, )):
            print('Se elimino producto')
        else:
            print('No se encontro producto')