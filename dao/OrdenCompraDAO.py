from models.Conectar import Conectar
from models.OrdenCompra import OrdenCompra

class OrdenCompraDAO:
    def __init__(self):
        self.__conectar = Conectar()

    def insertar_orden_compra(self, idCompra, idProducto, cantidad):
        orden_compra = OrdenCompra(idCompra, idProducto, cantidad)
        
        sql = """
            INSERT INTO orden_compra (idCompra, idProducto, cantidad) 
            VALUES (%s, %s, %s)
        """
        valores = (
            orden_compra.idCompra,
            orden_compra.idProducto,
            orden_compra.cantidad
        )
        
        if self.__conectar.ejecutar_sql(sql, valores):
            print('Se ha registrado la orden de compra en la base de datos')
        else:
            print('No se logró registrar la orden de compra')
    
    def listar_ordenes_compra(self):
        sql = '''
            SELECT idCompra, idProducto, cantidad
            FROM orden_compra
        '''
        listado = self.__conectar.listar(sql)
        if listado is not None:
            for orden in listado:
                print(f'ID Compra: {orden[0]}')
                print(f'ID Producto: {orden[1]}')
                print(f'Cantidad: {orden[2]}')
                print('------------------------------------')
    
    def modificar_cantidad_orden(self, idCompra, cantidad):
        buscar_orden = '''
            SELECT cantidad
            FROM orden_compra
            WHERE idCompra = %s
        '''
        orden = self.__conectar.listarUno(buscar_orden, (idCompra,))
        if orden:
            print('Orden de compra encontrada')
            modificar_orden = '''
                UPDATE orden_compra
                SET cantidad = %s
                WHERE idCompra = %s
            '''
            if self.__conectar.ejecutar_sql(modificar_orden, (cantidad, idCompra)):
                print('Cantidad de la orden de compra modificada')
            else:
                print('No se pudo modificar la cantidad de la orden de compra')
        else:
            print('Orden de compra no existe')
    
    def eliminar_orden_compra(self, idCompra):
        sql = '''
            DELETE FROM orden_compra
            WHERE idCompra = %s              
        '''
        if self.__conectar.ejecutar_sql(sql, (idCompra,)):
            print('Se eliminó la orden de compra')
        else:
            print('No se encontró la orden de compra')