# Punto de entrada de la aplicacion.
# Pendiente: implementar menu principal.

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
'''
Funcion que muestra el menu
'''
def mostrar_menu():
    print("=" * 60)
    print("\t Sistema Inventario de Productos")
    print("=" * 60)
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto por ID")
    print("5. Eliminar producto por ID")
    print("6. Reporte de bajo stock por cantidad")
    print("7. Salir")
    print("=" * 60)

'''
Funcion que captura opciones
'''
def capturar_opcion():
    entrada = input("Seleccione una opción (1-7): ")
    opcion = int(entrada)
    return opcion
           
if __name__ == "__main__":
    while True:
        try:
            mostrar_menu()
            opcion = capturar_opcion()
            print(f"Ha seleccionado la opción: {opcion}")
            if opcion < 1 or opcion > 7:
                print("Error: Opción fuera de rango. Intente nuevamente.")
                continue
            elif opcion == 1:
                while True:
                    nombre = input("Ingrese el nombre del producto a regitrar: ").lower().strip()
                    if nombre != "":
                        break
                    else:
                        print("El nombre es un campo obligatorio.")                    
                descripcion = input("Ingrese la descripcion del producto a regitrar (opcional, sino presione enter): ").lower().strip()
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad del producto a regitrar: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("Ha ingresado un número negativo, ingrese un número entero igual o mayor a cero.")
                    except ValueError:
                        print("Ha ingresado un valor inválido para cantidad, ingrese un valor numérico válido.")
                while True:
                    try:
                        precio = float(input("Ingrese el precio del producto a regitrar: "))
                        if precio >= 0:
                            break
                        else:
                            print("Ha ingresado un precio negativo, ingrese un precio igual o mayor a cero.")
                    except ValueError:
                        print("Ha ingresado un valor inválido para precio, ingrese un valor numérico válido.")
                categoria = input("Ingrese la categoria del producto a regitrar (opcional, sino presione enter): ").lower().strip()
                producto = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "cantidad" : cantidad,
                "precio" : precio,
                "categoria" : categoria
                }
                registrar_producto(producto)
                print(f"Producto {nombre.upper()} registrado correctamente.")
            elif opcion == 2:
                productos = mostrar_productos()
                print(productos)
            elif opcion == 3:
                while True:
                    try:
                        id = int(input("Ingrese el ID del producto a buscar: "))
                        if id > 0:
                            break
                        else:
                            print("Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print("Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_id = buscar_producto_por_id(id)
                if producto_id is not None:
                    print(producto_id)
                else: 
                    print(f"No existe producto con ID {id}")
            elif opcion == 4:
                while True:
                    try:
                        id = int(input("Ingrese el ID del producto que desea actualizar: "))
                        if id > 0:
                            break
                        else:
                            print("Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print("Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_actual = buscar_producto_por_id(id)
                if producto_actual is not None:
                    print(f"Actualizar producto: {producto_actual}")
                else:
                    print(f"No existe producto con ID {id}")
                    continue
                while True:
                    nombre = input("Ingrese el nombre del producto a actualizar: ").lower().strip()
                    if nombre != "":
                        break
                    else:
                        print("El nombre es un campo obligatorio.")                    
                descripcion = input("Ingrese la descripcion del producto a actualizar (opcional, sino presione enter): ").lower().strip()
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad del producto a actualizar: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("Ha ingresado un número negativo, ingrese un número entero igual o mayor a cero.")
                    except ValueError:
                        print("Ha ingresado un valor inválido para cantidad, ingrese un valor numérico válido.")
                while True:
                    try:
                        precio = float(input("Ingrese el precio del producto a actualizar: "))
                        if precio >= 0:
                            break
                        else:
                            print("Ha ingresado un precio negativo, ingrese un precio igual o mayor a cero.")
                    except ValueError:
                        print("Ha ingresado un valor inválido para precio, ingrese un valor numérico válido.")
                categoria = input("Ingrese la categoria del producto a actualizar (opcional, sino presione enter): ").lower().strip()
                producto = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "cantidad" : cantidad,
                "precio" : precio,
                "categoria" : categoria
                }
                actualizar_producto(id, producto)
                print(f"Producto ID {id} actualizado correctamente.")    
            elif opcion == 5:
                while True:
                    try:
                        id = int(input("Ingrese el ID del producto a eliminar: "))
                        if id > 0:
                            break
                        else:
                            print("Ha ingresado un número inválido para un ID. Ingrese un número entero mayor a cero")
                    except ValueError:
                        print("Ingreso un ID no válido. Ingrese un ID numérico válido.")
                producto_eliminar = buscar_producto_por_id(id)
                if producto_eliminar is not None:
                    print(producto_eliminar)
                    while True:
                            confirmacion = input(f"El producto ID {id} será eliminado, confirma? s/n: ")
                            if confirmacion == "s":
                                eliminar_producto(id)
                                print(f"Producto ID {id} eliminado.")
                                break
                            elif confirmacion == "n":
                                print(f"Eliminacion de producto ID {id} cancelada")
                                break
                            else:
                                print("Ha ingresado una opción no válida. Ingrese 's' si desea eliminar el producto o 'n' si desea cancelar la eliminación de producto.")
                else: 
                    print(f"No existe producto con ID {id}")
            elif opcion == 6:
                while True:
                    try:
                        limite = int(input("Ingrese la cantidad deseada para considerar stock bajo: "))
                        if limite >= 0:
                            stock_bajo = reporte_productos_bajo_stock(limite)
                            if stock_bajo != []:
                                print("=======")
                                print("ALERTA")
                                print("=======")
                                print("Productos con stock bajo: ")
                                print(stock_bajo)
                                break
                            elif stock_bajo == []:
                                print(f"No existen productos con cantidad igual o menor a {limite}")
                                break
                        else:
                                print("Ingrese un número válido para cantidad, entero positivo o cero.")
                    except:
                        print("Ha ingresado un valor no válido para cantidad límite")
            elif opcion == 7:
                print("Gracias por utilizar el sistema.")
                break
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número.")

    # =====================
    # PRUEBAS
    # =====================

    # Prueba de esqueleto antes de agregar CRUD
    # Casos a probar: 
    # opcion == a --> Debe entrar al except ValueError.
    # opcion == 10 --> Debe mostrar "opción fuera de rango".
    # opcion == 7 --> Debe salir del programa.
    # opcion == 1-6 -->  Debe mostrar "Ha seleccionado la opción: 1-6"

    # Prueba de alta correcta opcion 1 --> Registrar un producto y prueba de opcion 2 --> ver si persiste
    # Pruebas de validación de opción 1:
    # nombre vacío
    # cantidad = abc
    # cantidad = -1
    # cantidad = 0
    # precio = xyz
    # precio = -10
    # precio = 0 

    # Pruebas de validacion de opcion 3:
    # ID existente
    # ID inexistente
    # ID = 0
    # ID negativo
    # ID = abc