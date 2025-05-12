from dao.ProductoDAO import ProductoDAO
#from dao.ConserjeDAO import ConserjeDAO
import os
def generarTitulo(titulo):
    print(f'==== {titulo.upper()} ====')
    
def pausar():
    input("presione una tecla para continuar...")

def generarMenu(l):
    generarTitulo("Menu de acciones")
    for i, e in enumerate(l):
        print(f"{i+1}. {e.capitalize()}")
    print("0. Salir")
    try:
        opcion = int(input("Ingrese su opcion: "))
        if not(opcion >= 0 and opcion < len(l)+1):
            raise ValueError("La opcion no es valida.")
    except ValueError as e:
        print("error: ", e)
        input("Presione enter para continuar...")
        generarMenu(l)
    return opcion

def notVoid(msg):
    try:
        data = input(msg)
        if data == "":
            raise ValueError("El campo no puede estar vacio.")
            raise ValueError()
    except ValueError as e:
        print("error: ", e)
        notVoid(msg)
    return data.lower()

def isPositiveNumber(msg):
    try:
        data = int(input(msg))
        if data <= 0:
            raise ValueError("El numero no puede ser negativo ni 0.")
    except ValueError as e:
        print("error: ", e)
        isPositiveNumber(msg)
    return data

def isBoolean(msg):
    try:
        data = input(msg)
        if data != "s" and data != "n":
            raise ValueError("la respuesta debe ser S o N.")
    except ValueError as e:
        print("error: ", e)
        isBoolean(msg)
    return True if data == "s" else False

def agregarProducto():
    generarTitulo('Ingresando producto')
    #idProducto = notVoid('Ingrese codigo producto:\n')
    nombre = notVoid('Ingrese nombre de producto:\n')
    stock = isPositiveNumber('Ingrese stock de producto:\n')
    stockCritico = isPositiveNumber('Ingrese stock critico de producto:\n')
    habilitado = isBoolean("desea habilitar este producto en el inventario? (S/N)")

    dao = ProductoDAO()
    dao.insertar_producto(nombre, stock, stockCritico, habilitado)

def mostrarProductos():
    generarTitulo('listado de productos')
    dao = ProductoDAO()
    dao.listar_productos()

def actualizarProducto():
    generarTitulo('Actualizar producto')
    mostrarProductos()
    codigo = notVoid('Ingrese codigo a modificar:\n')
    subMenu = ["nombre de producto", "stock critico"]
    opcion = generarMenu(subMenu)
    dao = ProductoDAO()
    match(opcion):
        case 1:
            generarTitulo("modificar nombre")
            nombre = notVoid('Ingrese nuevo nombre:\n').capitalize()
            dao.modificarNombre(codigo, nombre)
        case 2:
            generarTitulo("modificar stock critico")
            stockCritico = isPositiveNumber('Ingrese nuevo stock critico:\n')
            dao.modificarStockCritico(codigo, stockCritico)
            
        case 0:
            pass
    pausar()

def eliminarProducto():
    mostrarProductos()
    generarTitulo('Eliminar productos')
    codigo = isPositiveNumber('Ingrese codigo a eliminar:\n')
    dao = ProductoDAO()
    dao.eliminar_producto(codigo)
    
menuAdministrador = ["agregar producto",
                     "mostrar listado productos",
                     "modificar producto",
                     "eliminar producto", 
                     "generar orden de compra", 
                     "modificar orden de compra", 
                     "eliminar reporte", 
                     "mostrar encargados", 
                     "habilitar encargado", 
                     "deshabilitar encargado", 
                     "agregar encargado", 
                     "eliminar encargado"
                     ]
menuEncargado = ["generar reporte", 
                 "modificar reporte", 
                 "mostrar solicitudes", 
                 "mostrar personal", 
                 "agregar personal", 
                 "eliminar personal"
                 ]
menuConserje = ["generar solicitud", 
                "modificar solicitud"
                ]
menuIniciarSesion = ["iniciar sesion como conserje", 
                     "iniciar sesion como encargado", 
                     "iniciar sesion como administrador", 
                     "olvide mi contraseña"
                     ]
opcion = generarMenu(menuAdministrador)
while not(opcion == 0):
    match(opcion):
        case 1:
            actualizarProducto()
    opcion = generarMenu(menuAdministrador)        
        
"""
while(opcion != 3):
    match(opcion):
        case 1: #as conserje
            generarTitulo('Iniciar sesion como conserje')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = ConserjeDAO()
            dao.iniciar_sesion(nombreUsuario, password)
            generarTitulo('Menu de conserje')
            opcionConserje = generarMenu(menuConserje)
            match(opcionConserje):
                case 1: #generar solicitud
                    pass
                case 2: #modificar solicitud
                    pass
                case 3: #mostrar solicitudes
                    generarTitulo('mostrar solicitudes')
                    dao.listar_solicitudes()
                case 3: #salir
                    pass
        case 2: #as encargado
            generarTitulo('Iniciar sesion como encargado')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = ConserjeDAO()
            dao.iniciar_sesion(nombreUsuario, password)
            generarTitulo('Menu de encargado')
            opcionEncargado = generarMenu(menuEncargado)
            match(opcionEncargado):
                case 1: #generar reporte
                    pass
                case 2: #modificar reporte
                    pass
                case 3: #mostrar solicitudes
                    pass
                case 4: #mostrar personal
                    pass
                case 5: #agregar personal
                    pass
                case 6: #eliminar personal
                    pass
        case 3: #as administrador
            generarTitulo('Iniciar sesion como administrador')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = ConserjeDAO()
            dao.iniciar_sesion(nombreUsuario, password)
            generarTitulo('Menu de administrador')
            opcionAdministrador = generarMenu(menuAdministrador)
            match(opcionAdministrador):
                case 1: #generar orden de compra
                    pass
                case 2: #modificar orden de compra
                    pass
                case 3: #eliminar reporte
                    pass
                case 4: #mostrar encargados
                    pass
                case 5: #habilitar encargado
                    pass
                case 6: #deshabilitar encargado
                    pass
                case 7: #agregar encargado
                    pass
                case 8: #eliminar encargado
                    pass
        case 4: #olvidar contraseña
            print("mala cuea")
            input("Por favor presione enter para continuar...")
            
    opcion = generarMenu(menuIniciarSesion)
"""