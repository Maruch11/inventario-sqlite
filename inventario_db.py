"""
Modulo que contiene la conexion a la base de datos
y las operaciones SQL sobre la tabla productos.
"""

# =====================
# IMPORT
# =====================

import sqlite3

# =======================
# CONEXION & CREATE TABLE
# =======================

# Inicializar variables globales en None para no arrastra efectos secundarios al importar el módulo
conexion = None # Crear variable global - scope del modulo
cursor = None # Crear variable global - scope del modulo

def init_db():
    """
    Inicializa la conexión a la base de datos y crea la tabla productos si no existe.
     Modifica las variables globales conexion y cursor para que estén disponibles
     en todo el módulo y puedan ser utilizadas por las funciones de acceso a datos.
     """
    global conexion, cursor # Modificar las variables del modulo, no crear variables locales
    conexion = sqlite3.connect("inventario.db") # Establecer conexión a la base de datos
    cursor = conexion.cursor() # Crear un objeto cursor para ejecutar sentencias SQL
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
    Devuelve una tupla (o None=) con los datos del producto cuyo ID coincide
    con el valor recibido como parámetro.
    """
    id_buscado = id
    cursor.execute('''
        SELECT *
        FROM productos
        WHERE id = ?
''', (id_buscado,)
)
    producto = cursor.fetchone()
    return producto

def select_all_by_like_nombre(nombre):
    """
    Devuelve una lista de tuplas con los productos cuyo
    nombre coincide con el patrón recibido.

    Función conservada como spike técnico.
    """
    nombre_buscado = f"%{nombre}%"
    cursor.execute('''
        SELECT * FROM productos 
        WHERE nombre like ?
''', (nombre_buscado,)
)
    filas = cursor.fetchall()
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

# ===============
# CERRAR CONEXION
# ===============
def cerrar_conexion():
    """Cierra la conexión a la base de datos.
     Modifica la variable global conexion para que no quede una conexión abierta."""
    global conexion, cursor
    conexion.close()
    conexion = None
    cursor = None