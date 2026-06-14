"""
Modulo que contiene la conexion a la base de datos
y las operaciones SQL sobre la tabla productos.
"""

# =====================
# IMPORT
# =====================

import sqlite3

# =====================
# CONEXION
# =====================

# Establecer conexión a la base de datos
conexion = sqlite3.connect("inventario.db") # variable global

# Crear un objeto cursor para ejecutar sentencias SQL
cursor = conexion.cursor() # variable global

# =====================
# CREATE TABLE
# =====================

# Crear tabla productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )  
''')

# ===========================
# FUNCIONES DE ACCESO A DATOS
# ===========================

# ----------------
# CONSULTAS (READ)
# ----------------

def select_all(): 
    """
    Devuelve una lista de tuplas con todos los registros de la tabla productos.
    """
    cursor.execute("SELECT * FROM productos") 
    filas = cursor.fetchall()
    return filas

def buscar_producto_por_id(id):
    """
    Devuelve una tupla con los datos del producto cuyo ID coincide
    con el valor recibido como parámetro.
    """
    id_buscado = id
    cursor.execute('''
        SELECT *
        FROM productos
        WHERE id = ?
''', (id_buscado,)
)
    filas = cursor.fetchone()
    return filas

def select_price_by_id(id):
    """
    Devuelve una tupla que contiene el precio del producto cuyo ID
    coincide con el valor recibido como parámetro.

    Función conservada como spike técnico.
    """
    id_buscado = id
    cursor.execute('''
        SELECT precio 
        FROM productos 
        WHERE id = ?
''', (id_buscado,)
)
    filas = cursor.fetchone()
    return filas

def select_price_by_like_nombre(nombre):
    """
    Devuelve una tupla que contiene el precio del primer producto cuyo
    nombre coincide con el patrón recibido.

    Función conservada como spike técnico.
    """
    nombre_buscado = f"%{nombre}%"
    cursor.execute('''
        SELECT precio 
        FROM productos 
        WHERE nombre like ?
''', (nombre_buscado,)
)
    filas = cursor.fetchone()
    return filas

# --------------
# ALTAS (CREATE)
# --------------

def registrar_producto(producto):
    """
    Inserta un nuevo producto en la tabla productos y persiste
    los cambios en la base de datos.

    Devuelve la cantidad de filas afectadas.
    """
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
''', (
    producto["nombre"],
    producto["descripcion"],
    producto["cantidad"],
    producto["precio"],
    producto["categoria"]
    ))
    conexion.commit()
    return cursor.rowcount

# -----------------------
# MODIFICACIONES (UPDATE)
# -----------------------

def actualizar_producto(id, producto):
    """
    Actualiza todos los campos del producto cuyo ID coincide
    con el valor recibido como parámetro.

    Devuelve la cantidad de filas afectadas.
    """
    cursor.execute('''
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
''', (
    producto["nombre"],
    producto["descripcion"],
    producto["cantidad"],
    producto["precio"],
    producto["categoria"],
    id
    ))
    conexion.commit()
    return cursor.rowcount

def actualizar_precio_by_id(id, precio):
    """
    Actualiza el precio del producto cuyo ID coincide con el valor
    recibido como parámetro.

    Devuelve la cantidad de filas afectadas.

    Función conservada como spike técnico.
    """
    id_buscado = id
    precio_actualizado = precio
    cursor.execute('''
        UPDATE productos
        SET precio = ?
        WHERE id = ?
''', (precio_actualizado, id_buscado))
    conexion.commit()
    return cursor.rowcount

# --------------
# BAJAS (DELETE)
# --------------

def eliminar_producto_by_id(id):
    """
    Elimina el producto cuyo ID coincide con el valor recibido
    como parámetro.

    Devuelve la cantidad de filas afectadas.
    """
    id_buscado = id
    cursor.execute('''
        DELETE FROM productos WHERE id = ?
''', (id_buscado,))
    conexion.commit()
    return cursor.rowcount

# --------
# REPORTES
# --------

def reporte_productos_bajo_stock(cantidad):
    """
    Devuelve una lista de tuplas con los productos cuya cantidad
    es menor o igual al límite recibido como parámetro.
    """
    cantidad_limite = cantidad
    cursor.execute('''
    SELECT *
    FROM productos
    WHERE cantidad <= ?
''', (cantidad_limite,))
    filas = cursor.fetchall()
    return filas