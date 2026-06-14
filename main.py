"""
Modulo principal de la aplicacion.

Gestiona la interaccion con el usuario mediante un menu
de opciones para administrar productos del inventario.
"""

# =====================
# IMPORT
# =====================
from colorama import Fore, init

from inventario_service import (
    mostrar_productos,
    registrar_producto,
    buscar_producto_por_id,
    actualizar_producto,
    eliminar_producto,
    reporte_productos_bajo_stock
)

init(autoreset=True)

# =====================
# funciones 
# =====================

def mostrar_menu():
    """
    Muestra el menú principal de opciones del sistema.
    """
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.CYAN + "\t Sistema Inventario de Productos")
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.CYAN + "1. Registrar producto")
    print(Fore.CYAN + "2. Mostrar productos")
    print(Fore.CYAN + "3. Buscar producto por ID")
    print(Fore.CYAN + "4. Actualizar producto por ID")
    print(Fore.CYAN + "5. Eliminar producto por ID")
    print(Fore.CYAN + "6. Reporte de bajo stock por cantidad")
    print(Fore.CYAN + "7. Salir")
    print(Fore.MAGENTA + "=" * 60)

def capturar_opcion():
    """
    Captura y devuelve como entero la opción ingresada por el usuario.
    """
    entrada = input("Seleccione una opción (1-7): ")
    opcion = int(entrada)
    return opcion

# =====================
# Programa
# =====================      
if __name__ == "__main__":
    while True:
        try:
            mostrar_menu()
            opcion = capturar_opcion()
            print(Fore.BLUE + f"Ha seleccionado la opción: {opcion}")
            if opcion < 1 or opcion > 7:
                print(Fore.RED + "Error: Opción fuera de rango. Intente nuevamente.")
                continue
            elif opcion == 1:
                while True:
                    nombre = input(Fore.BLUE + "Ingrese el nombre del producto a regitrar: ").lower().strip()
                    if nombre != "":
                        break
                    else:
                        print(Fore.RED + "El nombre es un campo obligatorio.")                    
                descripcion = input(Fore.BLUE + "Ingrese la descripcion del producto a regitrar (opcional, sino presione enter): ").lower().strip()
                while True:
                    try:
                        cantidad = int(input(Fore.BLUE + "Ingrese la cantidad del producto a regitrar: "))
                        if cantidad >= 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un número negativo, ingrese un número entero igual o mayor a cero.")
                    except ValueError:
                        print(Fore.RED + "Ha ingresado un valor inválido para cantidad, ingrese un valor numérico válido.")
                while True:
                    try:
                        precio = float(input(Fore.BLUE + "Ingrese el precio del producto a regitrar: "))
                        if precio >= 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un precio negativo, ingrese un precio igual o mayor a cero.")
                    except ValueError:
                        print(Fore.RED + "Ha ingresado un valor inválido para precio, ingrese un valor numérico válido.")
                categoria = input(Fore.BLUE + "Ingrese la categoria del producto a regitrar (opcional, sino presione enter): ").lower().strip()
                producto = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "cantidad" : cantidad,
                "precio" : precio,
                "categoria" : categoria
                }
                registrar_producto(producto)
                print(Fore.GREEN + f"Producto {nombre.upper()} registrado correctamente.")
            elif opcion == 2:
                productos = mostrar_productos()
                print(productos)
            elif opcion == 3:
                while True:
                    try:
                        id = int(input(Fore.BLUE + "Ingrese el ID del producto a buscar: "))
                        if id > 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print(Fore.RED + "Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_id = buscar_producto_por_id(id)
                if producto_id is not None:
                    print(producto_id)
                else: 
                    print(Fore.BLUE + f"No existe producto con ID {id}")
            elif opcion == 4:
                while True:
                    try:
                        id = int(input(Fore.BLUE + "Ingrese el ID del producto que desea actualizar: "))
                        if id > 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print(Fore.RED + "Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_actual = buscar_producto_por_id(id)
                if producto_actual is not None:
                    print(Fore.BLUE + f"Actualizar producto: {producto_actual}")
                else:
                    print(Fore.BLUE + f"No existe producto con ID {id}")
                    continue
                while True:
                    nombre = input(Fore.BLUE + "Ingrese el nombre del producto a actualizar: ").lower().strip()
                    if nombre != "":
                        break
                    else:
                        print(Fore.RED + "El nombre es un campo obligatorio.")                    
                descripcion = input(Fore.BLUE + "Ingrese la descripcion del producto a actualizar (opcional, sino presione enter): ").lower().strip()
                while True:
                    try:
                        cantidad = int(input(Fore.BLUE + "Ingrese la cantidad del producto a actualizar: "))
                        if cantidad >= 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un número negativo, ingrese un número entero igual o mayor a cero.")
                    except ValueError:
                        print(Fore.RED + "Ha ingresado un valor inválido para cantidad, ingrese un valor numérico válido.")
                while True:
                    try:
                        precio = float(input(Fore.BLUE + "Ingrese el precio del producto a actualizar: "))
                        if precio >= 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un precio negativo, ingrese un precio igual o mayor a cero.")
                    except ValueError:
                        print(Fore.RED + "Ha ingresado un valor inválido para precio, ingrese un valor numérico válido.")
                categoria = input(Fore.BLUE + "Ingrese la categoria del producto a actualizar (opcional, sino presione enter): ").lower().strip()
                producto = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "cantidad" : cantidad,
                "precio" : precio,
                "categoria" : categoria
                }
                actualizar_producto(id, producto)
                print(Fore.GREEN + f"Producto ID {id} actualizado correctamente.")    
            elif opcion == 5:
                while True:
                    try:
                        id = int(input(Fore.BLUE + "Ingrese el ID del producto a eliminar: "))
                        if id > 0:
                            break
                        else:
                            print(Fore.RED + "Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print(Fore.RED + "Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_eliminar = buscar_producto_por_id(id)
                if producto_eliminar is not None:
                    print(producto_eliminar)
                    while True:
                            confirmacion = input(Fore.BLUE + f"El producto ID {id} será eliminado, confirma? s/n: ")
                            if confirmacion == "s":
                                eliminar_producto(id)
                                print(Fore.GREEN + f"Producto ID {id} eliminado.")
                                break
                            elif confirmacion == "n":
                                print(Fore.BLUE + f"Eliminacion de producto ID {id} cancelada")
                                break
                            else:
                                print(Fore.RED + "Ha ingresado una opción no válida. Ingrese 's' si desea eliminar el producto o 'n' si desea cancelar la eliminación de producto.")
                else: 
                    print(Fore.BLUE + f"No existe producto con ID {id}")
            elif opcion == 6:
                while True:
                    try:
                        limite = int(input(Fore.BLUE + "Ingrese la cantidad deseada para considerar stock bajo: "))
                        if limite >= 0:
                            stock_bajo = reporte_productos_bajo_stock(limite)
                            if stock_bajo != []:
                                print(Fore.BLUE + "=======")
                                print(Fore.BLUE + "ALERTA")
                                print(Fore.BLUE + "=======")
                                print(Fore.BLUE + "Productos con stock bajo: ")
                                print(stock_bajo)
                                break
                            elif stock_bajo == []:
                                print(Fore.BLUE + f"No existen productos con cantidad igual o menor a {limite}")
                                break
                        else:
                                print(Fore.RED + "Ingrese un número válido para cantidad, entero positivo o cero.")
                    except:
                        print(Fore.RED + "Ha ingresado un valor no válido para cantidad límite")
            elif opcion == 7:
                print(Fore.YELLOW + "Gracias por utilizar el sistema.")
                break
        except ValueError:
            print(Fore.RED + "Error: Entrada no válida. Debe ingresar un número.")