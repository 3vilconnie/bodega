from dao.ProductoDAO import ProductoDAO
import os

def generaMenu(l):
    print('==== Menu de acciones ====')
    for i, e in enumerate(l):
        print(f"{i+1}. {e.capitalize()}")
    opcion = int(input("Ingrese su opcion: "))
    while not(opcion > 0 and opcion < len(l)+1):
        print("ingrese una opcion valida.")
        opcion = int(input("Ingrese su opcion: "))
    return opcion

def agregarProducto():
    print('==== Ingresando producto ====')
    codigo = input('Ingrese codigo producto:\n').lower() # abc 
    nombre = input('Ingrese nombre de producto:\n').capitalize()
    precio = float(input('Ingrese precio de producto:\n'))
    stock = int(input('Ingrese stock de producto:\n'))    
    dao = ProductoDAO()
    dao.insertar_producto(codigo, nombre, precio, stock)

def mostrarProductos():
    print('==== Mostrar producto ====')
    dao = ProductoDAO()
    dao.listar_productos()

def actualizarProducto():
    print('==== Actualizar producto ====')
    # buscar un producto
    codigo = input('Ingrese codigo a modificar:\n').lower()
    # nuevo nombre producto
    nombre = input('Ingrese nuevo nombre:\n').capitalize()
    dao = ProductoDAO()
    dao.modificar_nombre_producto(codigo, nombre)    

def eliminarProducto():
    print('==== Eliminar productos ====')
    codigo = input('Ingrese codigo a eliminar:\n').lower()
    dao = ProductoDAO()
    dao.eliminar_producto(codigo)
    
menuAdministrador = ["generar orden de compra", "modificar orden de compra", "eliminar reporte", "mostrar encargados", "habilitar encargado", "deshabilitar encargado", "agregar encargado", "eliminar encargado", "salir"]
menuEncargado = ["generar reporte", "modificar reporte", "mostrar solicitudes", "mostrar personal", "agregar personal", "eliminar personal", "salir"]
menuConserje = ["generar solicitud", "modificar solicitud", "salir"]
menuIniciarSesion = ["iniciar sesion como conserje", "iniciar sesion como encargado", "iniciar sesion como administrador", "olvide mi contraseña", "salir"]
opcion = generaMenu(menuIniciarSesion)

while(opcion != 3):
    match(opcion):
        case 1: #login
            pass
        case 2: #forgot password
            pass
        case 3: #exit
            pass
        case _:
            pass
            
    opcion = generaMenu(menuIniciarSesion)

"""
while(opcion != 0):
    os.system('cls') # Limpia consola
    match(opcion):
        case 1: #add
            agregarProducto()    
            break
        case 2: #show
            mostrarProductos()
            break
        case 3: #update
            actualizarProducto()    
            break  
        case 4: #delete
            eliminarProducto
            break    
        case 0: #exit
            print('Saliendo sistema...')                
            input('Presione enter para continuar...')
            break
    opcion = generaMenu(menu)
"""