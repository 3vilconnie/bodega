from models.Conectar import Conectar
from models.Proveedor import Proveedor

class ProveedorDAO:
    def __init__(self):
        self.__conectar = Conectar()
        
    def insertar_proveedor(self, idProveedor, nombreProveedor, email):
        proveedor = Proveedor(idProveedor, nombreProveedor, email)
        
        sql = """
            INSERT INTO proveedor (idProveedor, nombreProveedor, email) 
            VALUES (%s, %s, %s)
        """
        valores = (
            proveedor.idProveedor,
            proveedor.nombreProveedor,
            proveedor.email
        )
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado el proveedor en la base de datos')
        else:
            print('No se logró registrar el proveedor')
            
    def listar_proveedores(self):
        sql = '''
            SELECT idProveedor, nombreProveedor, email
            FROM proveedor
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for proveedor in listado:
                print(f'ID Proveedor: {proveedor[0]}')
                print(f'Nombre Proveedor: {proveedor[1]}')
                print(f'Email: {proveedor[2]}')
                print('------------------------------------')
        
    def modificar_nombre_proveedor(self, idProveedor, nombreProveedor):
        buscar_proveedor = '''
            SELECT nombreProveedor
            FROM proveedor
            WHERE idProveedor = %s
        '''
        proveedor = self.__conectar.listarUno(buscar_proveedor, (idProveedor,))
        if proveedor:
            print('Proveedor encontrado')
            modificar_proveedor = '''
                UPDATE proveedor
                SET nombreProveedor = %s
                WHERE idProveedor = %s
            '''
            if self.__conectar.ejecutar_sql(modificar_proveedor, (nombreProveedor, idProveedor)):
                print('Proveedor modificado')
            else:
                print('Proveedor no se pudo modificar')
        else:
            print('Proveedor no existe')
            
    def eliminar_proveedor(self, idProveedor):
        sql = '''
            DELETE FROM proveedor
            WHERE idProveedor = %s              
        '''
        if self.__conectar.ejecutar_sql(sql, (idProveedor,)):
            print('Se eliminó el proveedor')
        else:
            print('No se encontró el proveedor')