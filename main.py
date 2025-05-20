import datetime
import os

from dao.SolicitudDAO import SolicitudDAO
from dao.EncargadoDAO import EncargadoDAO
from dao.ConserjeDAO import ConserjeDAO
from dao.AdministradorDAO import AdministradorDAO
from dao.ProductoDAO import ProductoDAO
from dao.EstanteriaDAO import EstanteriaDAO
def generarTitulo(titulo):
    print(f'==== {titulo.upper()} ====')

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pausar():
    input("presione una tecla para continuar...")

def generarMenu(l):
    limpiarPantalla()
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
    pausar()

def mostrarProductos():
    generarTitulo('listado de productos')
    dao = ProductoDAO()
    dao.listar_productos()
    pausar()

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
                 "eliminar personal",
                 "agregar estanteria",
                 "modificar estanteria",
                 "eliminar estanteria",
                 ]
menuConserje = ["generar solicitud", 
                "modificar solicitud",
                "listar solicitudes"
                ]
menuIniciarSesion = ["iniciar sesion como conserje", 
                     "iniciar sesion como encargado", 
                     "iniciar sesion como administrador", 
                     "olvide mi contraseña"
                     ]  

opcion = generarMenu(menuIniciarSesion)
while(opcion != 0):
    match(opcion):
        case 1: #as conserje
            generarTitulo('Iniciar sesion como conserje')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = ConserjeDAO()
            usuario = dao.iniciar_sesion(nombreUsuario, password)
            print(usuario)
            if usuario != None:
                generarTitulo('Menu de conserje')
                opcionConserje = generarMenu(menuConserje)
                while(opcionConserje != 0):
                    match(opcionConserje):
                        case 1: #generar solicitud
                            dSolicitud = SolicitudDAO()
                            generarTitulo('Generar solicitud')
                            fecha_hoy = datetime.date.today()
                            solicitud = dSolicitud.insertar_solicitud(fecha_hoy, usuario._rut)
                            print(f"Solicitud generada con fecha: {fecha_hoy} y rut: {usuario._rut}")
                            idSolicitud = dao.id_ultima_solicitud(usuario._rut)
                            agregar = True
                            while(agregar):
                                limpiarPantalla()
                                ProductoDAO().listar_productos()
                                print("Ingrese el id de productos a agregar a la solicitud")
                                idProducto = isPositiveNumber("Ingrese el id del producto a agregar:\n")
                                cantidad = isPositiveNumber("Ingrese la cantidad:\n")
                                dSolicitud.agregarProducto(idSolicitud, idProducto, cantidad)
                                agregar = isBoolean("quiere agregar otro producto? (s/n)")
                            pausar()
                        case 2: #modificar solicitud
                            pass
                        case 3: #mostrar solicitudes
                            generarTitulo('mostrar solicitudes')
                            dao.listar_solicitudes(usuario._rut)
                            pausar()
                    
                    opcionConserje = generarMenu(menuConserje)

        case 2: #as encargado
            generarTitulo('Iniciar sesion como encargado')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = EncargadoDAO()
            usuario = dao.iniciar_sesion(nombreUsuario, password)
            if usuario != None:
                generarTitulo('Menu de encargado')
                opcionEncargado = generarMenu(menuEncargado)
                while(opcionEncargado != 0):
                    match(opcionEncargado):
                        case 1: #generar reporte
                            pass
                        case 2: #modificar reporte
                            pass
                        case 3: #mostrar solicitudes
                            generarTitulo('mostrar solicitudes')
                            dao.listar_solicitudes(usuario._rut)
                            pausar()
                        case 4: #mostrar personal
                            generarTitulo('mostrar personal')
                            print("encargado: ", usuario._rut)
                            dao.listar_personal(usuario._rut)
                            pausar()
                        case 5: #agregar personal
                            generarTitulo('Agregar personal')
                            ConserjeDAO().listar_conserjes_sin_asignar()
                            rut = notVoid('Ingrese rut de la persona:\n')
                            ConserjeDAO().asignar_encargado(rut, usuario._rut)
                            pausar()
                        case 6: #eliminar personal
                            generarTitulo('Eliminar personal')
                            dao.listar_personal(usuario._rut)
                            rut = notVoid('Ingrese rut de la persona a eliminar:\n')
                            dao.desvincular_conserje(rut)
                            pausar()
                        case 7: #agregar estanteria
                            estanteriadao = EstanteriaDAO()
                            generarTitulo('Agregar estanteria')
                        case 8: #modificar estanteria
                            pass
                        case 9: #eliminar estanteria
                            pass
                    opcionEncargado = generarMenu(menuEncargado)
        case 3: #as administrador
            generarTitulo('Iniciar sesion como administrador')
            nombreUsuario = notVoid('Ingrese su nombre de usuario:\n')
            password = notVoid('Ingrese su contraseña:\n')
            dao = AdministradorDAO()
            if dao.iniciar_sesion(nombreUsuario, password):
                generarTitulo('Menu de administrador')
                opcionAdministrador = generarMenu(menuAdministrador)
                while(opcionAdministrador != 0):
                    match(opcionAdministrador):
                        case 1: #agregar producto
                            agregarProducto()
                        case 2: #mostrar listado productos
                            mostrarProductos()
                            pausar()
                        case 3: #modificar producto
                            actualizarProducto()
                        case 4: #eliminar producto
                            pass
                        case 5: #generar orden de compra
                            pass
                        case 6: #modificar orden de compra
                            pass
                        case 7: #eliminar reporte
                            pass
                        case 8: #mostrar encargados
                            encargadodao = EncargadoDAO()
                            encargadodao.listar_encargados()
                            pausar()
                        case 9: #habilitar encargado
                            encargadodao = EncargadoDAO()
                            encargadodao.listar_encargados()
                            rut = notVoid("ingrese rut del encargado a habilitar:\n")
                            dao.habilitar_encargado(rut)
                            pausar()
                        case 10: #deshabilitar encargado
                            encargadodao = EncargadoDAO()
                            encargadodao.listar_encargados()
                            rut = notVoid("ingrese rut del encargado a deshabilitar:\n")
                            dao.deshabilitar_encargado(rut)
                            pausar()
                        case 11: #agregar encargado
                            generarTitulo('Agregar encargado')
                            nombre = notVoid('Ingrese nombre de encargado:\n')
                            apellido = notVoid('Ingrese apellido de encargado:\n')
                            email = notVoid('Ingrese email de encargado:\n')
                            rut = notVoid('Ingrese rut de encargado:\n')
                            password = notVoid('Ingrese contraseña de encargado:\n')
                            nombreUsuario = notVoid('Ingrese nombre de usuario de encargado:\n')
                            EncargadoDAO().insertar_encargado(nombreUsuario, password, nombre, apellido, email, rut)
                            pausar()
                        case 12: #eliminar encargado
                            pass
                    opcionAdministrador = generarMenu(menuAdministrador)
            else:
                print("usuario o contraseña incorrectos")
                pausar()
        case 4: #olvidar contraseña
            print("mala cuea")
            input("Por favor presione enter para continuar...")
            
    opcion = generarMenu(menuIniciarSesion)
