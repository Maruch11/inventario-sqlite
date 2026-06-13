'''
Este modulo contiene la conexion a la base de datos
y las operaciones SQL sobre la tabla productos.
'''
# =====================
# IMPORT
# =====================

import sqlite3

# =====================
# CONEXION
# =====================

# Establecer conexión a la base de datos
conexion = sqlite3.connect("inventario.db") # variable global

# Crear un objeto cursor
'''
El método cursor() permite obtener un objeto cursor, 
que es necesario para ejecutar comandos SQL.
'''
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

# =====================
# funciones CRUD
# =====================

# Consulta select_all from productos
def select_all():   
    cursor.execute("SELECT * FROM productos") 
    filas = cursor.fetchall()
    return filas

# obtener_producto por ID
'''
Funcion que devuelve todos los campos de la tabla productos consultando por campo ID
'''
def buscar_producto_por_id(id):
    id_buscado = id
    cursor.execute('''
        SELECT *
        FROM productos
        WHERE id = ?
''', (id_buscado,)
)
    filas = cursor.fetchone()
    return filas

# Consulta precio por ID
'''
Funcion que devuelve el precio consultando por LIKE nombre 
'''
def select_price_by_id(id):
    id_buscado = id
    cursor.execute('''
        SELECT precio 
        FROM productos 
        WHERE id = ?
''', (id_buscado,)
)
    filas = cursor.fetchone()
    return filas

# Consulta precio por LIKE nombre
'''
Funcion que devuelve el precio consultando por ID 
'''
def select_price_by_like_nombre(nombre):
    nombre_buscado = f"%{nombre}%"
    cursor.execute('''
        SELECT precio 
        FROM productos 
        WHERE nombre like ?
''', (nombre_buscado,)
)
    filas = cursor.fetchone()
    return filas

# registrar_producto
'''
Funcion que recibe un diccionario,
ejecuta un INSERT,
hace commit(),
devuelve cursor.rowcount.
'''
def registrar_producto(producto):
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

# actualizar_producto por ID
def actualizar_producto(id, producto):
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

# actualizar_ precio por ID
'''
Funcion que actualiza precio de un campo precio de la tabla productos filtrando por campo ID
'''
def actualizar_precio_by_id(id, precio):
    id_buscado = id
    precio_actualizado = precio
    cursor.execute('''
        UPDATE productos
        SET precio = ?
        WHERE id = ?
''', (precio_actualizado, id_buscado))
    conexion.commit()
    return cursor.rowcount

# Eliminar_producto por ID
def eliminar_producto_by_id(id):
    id_buscado = id
    cursor.execute('''
        DELETE FROM productos WHERE id = ?
''', (id_buscado,))
    conexion.commit()
    return cursor.rowcount

# Reporte productos cantidad limite inferior
def reporte_productos_bajo_stock(cantidad):
    cantidad_limite = cantidad
    cursor.execute('''
    SELECT *
    FROM productos
    WHERE cantidad <= ?
''', (cantidad_limite,))
    filas = cursor.fetchall()
    return filas

if __name__ == "__main__":
    # =====================
    # PRUEBAS
    # =====================

    # print("Conexión establecida exitosamente")
    # print("Objeto cursor creado exitosamente")

    # print("Tabla 'productos' creada exitosamente")

    # Insertar datos en la tabla
    # cursor.execute('''
    #     INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
    #     VALUES (?, ?, ?, ?, ?)
    # ''', ("Sapiens", "Historia de la humanidad", 5, 25000, "Historia"))

    # print("Productos agregados exitosamente")

    # cursor.executemany('''
    #     INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
    #     VALUES (?, ?, ?, ?, ?)
    # ''', [
    #         ("Inteligencia Artificial", "Introducción a la IA moderna", 3,	32000, "IA"), 
    #         ("Deep Learning",	"Redes neuronales profundas", 2, 45000,	"IA"),
    #         ("Python para Ciencia de Datos", "Programación aplicada", 4, 28000,	"Programación"),
    #         ("Homo Deus", "Futuro de la humanidad", 6, 27000, "Tecnología")
    #     ]
    # )

    # print("Productos agregados exitosamente") - lineas comentadas despues de ejecucion para evitar duplicacion de inserciones

    # Consultar todos los productos
    print(select_all())

    # Buscar producto por ID
    # print(buscar_producto_por_id(1))

    # # Buscar precio por ID
    # print(select_price_by_id(1))

    # # Buscar precio por LIKE nombre
    # print(select_price_by_like_nombre("IA"))

    # actualizar_precio_by_id(3, 50000)
    # print(buscar_producto_por_id(3))

    # eliminar_producto_by_id(3)
    # print(buscar_producto_por_id(3))

    # Buscar productos por cantidad limite
    # print(reporte_productos_bajo_stock(4))

    # Prueba de registrar_producto
    # producto_prueba = {
    #     "nombre" : "Deep Learning",	
    #     "descripcion" : "Redes neuronales profundas", 
    #     "cantidad" : 2, 
    #     "precio" : 45000,	
    #     "categoria" : "IA"
    # }

    # registrar_producto(producto_prueba)
    # print(select_all())

    # Prueba de actualizar_producto
    # producto_prueba = {
    #     "nombre" : "Deep Learning",	
    #     "descripcion" : "Redes neuronales profundas", 
    #     "cantidad" : 8, 
    #     "precio" : 80000,	
    #     "categoria" : "IA"
    # }

    # actualizar_producto(6, producto_prueba)
    # print(select_all())
    
    # =====================
    # COMMIT & CLOSE
    # =====================

    # Confirmar los cambios
    conexion.commit()
    print("Cambios persistidos exitosamente")

    # Cerrar la conexión
    conexion.close()
    print("Conexion cerrada exitosamente")