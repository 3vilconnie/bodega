from models.Conectar import Conectar
from models.Producto import Producto # Importa clase Conectar dentro de ProductoDAO

class ProductoDAO:
    def __init__(self):
        self.__conectar = Conectar() # Instancia objeto Conectar para ejecutar conexion a base de datos
        
    def insertar_producto(self, idProducto, nombreProducto, stock, stockCritico, disponible):
        # Instanciar Producto
        producto = Producto(idProducto, nombreProducto, stock, stockCritico, disponible)
        
        # Utilizando SQL para insertar nuevos datos
        sql = """
            INSERT INTO producto (idProducto, nombreProducto, stock, stockCritico, disponible) 
            VALUES (%s, %s, %s, %s, %s)
            """
        # Crear tupla de datos con objeto producto 
        valores = (
            producto.idProducto, 
            producto.nombreProducto, 
            producto.stock, 
            producto.stockCritico, 
            producto.disponible
        )
        
        # Ejecutando sentencia sql DEVUELVE TRUE o FALSE
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el producto en la base de datos')
        else:
            print('No se logro registrar el producto')
            
    def listar_productos(self):
        sql = '''
            SELECT idProducto, nombreProducto, stock, stockCritico, disponible
            FROM producto
            '''
        listado = self.__conectar.listar(sql) # [(codigo, nombre, precio, stock), (, , , )]
        if listado is not None:      #                0       1       2      3
            for producto in listado: # producto -> (codigo, nombre, precio, stock)
                print(f'Codigo producto: {producto[0]}')
                print(f'Nombre: {producto[1]}')
                print(f'stock: {producto[2]}')
                print(f'Stock critico: {producto[3]}')
                print(f'disponible: {producto[4]}')
            
                print('------------------------------------')
                
    def eliminar_producto(self, idProducto):
        sql = """
            SELECT nombre FROM producto
            WHERE idProducto = %s
        """
        if(self.__conectar.listarUno(sql, (idProducto, )) != None):
            sql = '''
                    DELETE FROM producto
                    WHERE idProducto = %s
                    '''
            if self.__conectar.ejecutar_sql(sql, (idProducto, )):
                print('Se elimino producto')
            else:
                print('No se encontro producto')
        else:
            print(f"error al eliminar producto {idProducto}")
        
    def modificarNombre(self, idProducto, nuevoNombre):
        sql = """
        SELECT nombre FROM producto WHERE idProducto = %s
        """
        valores = (nuevoNombre, idProducto)
        
        if self.__conectar.listarUno(sql, (idProducto, )) != None:
            sql = """
            UPDATE producto
            SET nombre = %s WHERE idProducto = %s
            """
            
            self.__conectar(sql, valores)
        else:
            print(f"no se pude modificar nombre de producto({idProducto}) por {nuevoNombre}!!!")
    
    def modificarStockCritico(self, idProducto, nuevoStock):
        sql = """
        SELECT nombre FROM producto WHERE idProducto = %s
        """
        valores = (nuevoStock, idProducto)
        
        if self.__conectar.listarUno(sql, (idProducto, )) != None:
            sql = """
            UPDATE producto
            SET stockCritico = %s WHERE idProducto = %s
            """
            
            self.__conectar(sql, valores)
        else:
            print(f"no se pude modificar el stock critico producto({idProducto}) por {nuevoStock}!!!")
    
    def agregarStock(self, idProducto, cantidad):
        sql = """
        SELECT nombre FROM producto WHERE idProducto = %s
        """
        tupla = self.__conectar.listarUno(sql, (idProducto, ))
        stock = int(tupla[2]) + cantidad
        valores = (str(stock), idProducto)
        
        if tupla != None:
            sql = """
            UPDATE producto
            SET stock = %s WHERE idProducto = %s
            """
            
            self.__conectar(sql, valores)
        else:
            print(f"error al agregar stock producto({idProducto}) {cantidad} unidades!!!")
    
    def habilitar(self, idProducto):
        sql = """
        SELECT nombre FROM producto WHERE idProducto = %s
        """
        valores = (idProducto, )
        
        if self.__conectar.listarUno(sql, (idProducto, )) != None:
            sql = """
            UPDATE producto
            SET habilitado = True WHERE idProducto = %s
            """
            
            self.__conectar(sql, valores)
        else:
            print("no se pude habilitar producto!!!")
    
    def deshabilitar(self, idProducto):
        sql = """
        SELECT nombre FROM producto WHERE idProducto = %s
        """
        valores = (idProducto, )
        
        if self.__conectar.listarUno(sql, (idProducto, )) != None:
            sql = """
            UPDATE producto
            SET habilitado = False WHERE idProducto = %s
            """
            
            self.__conectar(sql, valores)
        else:
            print("no se pude deshabilitar producto!!!")