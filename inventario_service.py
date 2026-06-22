"""
Modulo que implementa la capa de servicios y actua como
pasarela entre la capa de presentacion y la capa de acceso a datos.
"""

# =====================
# IMPORT
# =====================
import inventario_db

# =====================
# funciones pasarela
# =====================

def inicializar():
    """
    Inicializa la base de datos, crea un objeto cursor y crea la tabla productos si no existe.
     """
    inventario_db.init_db()

def mostrar_productos():
    """
    Devuelve una lista de tuplas con todos los registros
    de la tabla productos.
    """
    return inventario_db.select_all()

def buscar_producto_por_id(id):
    """
    Devuelve el producto cuyo ID coincide con el valor
    recibido como parámetro.
    """
    return inventario_db.buscar_producto_por_id(id)

def buscar_productos_por_nombre(nombre):
    """
    Devuelve una lista de tuplas con los productos cuyo
    nombre coincide con el valor recibido como parámetro.
    Función conservada como spike técnico.
    """
    return inventario_db.select_all_by_like_nombre(nombre)

def registrar_producto(producto):
    """
    Registra un nuevo producto utilizando la capa
    de acceso a datos.
    """
    return inventario_db.registrar_producto(producto)

def actualizar_producto(id, producto):
    """
    Actualiza todos los campos del producto cuyo ID coincide
    con el valor recibido como parámetro.
    """
    return inventario_db.actualizar_producto(id, producto)

def eliminar_producto(id):
    """
    Elimina el producto cuyo ID coincide con el valor
    recibido como parámetro.
    """
    return inventario_db.eliminar_producto_by_id(id)

def reporte_productos_bajo_stock(cantidad):
    """
    Devuelve una lista de tuplas con los productos cuya cantidad
    es menor o igual al límite recibido como parámetro.
    """
    return inventario_db.reporte_productos_bajo_stock(cantidad)

def cerrar():
    """Cierra la conexión a la base de datos."""
    inventario_db.cerrar_conexion()