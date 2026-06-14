# Capa de servicios de negocio.
# Orquestación de las operaciones de inventario_db.py.
# =====================
# IMPORT
# =====================
import inventario_db

# =====================
# funciones pasarela
# =====================
def mostrar_productos():
    return inventario_db.select_all()

def registrar_producto(producto):
    return inventario_db.registrar_producto(producto)

def buscar_producto_por_id(id):
    return inventario_db.buscar_producto_por_id(id)

def actualizar_producto(id, producto):
    return inventario_db.actualizar_producto(id, producto)

# def actualizar_precio(id, precio):
#     return actualizar_precio_by_id(id, precio)
# funcion spike no hace falta presentar en el final

def eliminar_producto(id):
    return inventario_db.eliminar_producto_by_id(id)

def reporte_productos_bajo_stock(cantidad):
    return inventario_db.reporte_productos_bajo_stock(cantidad)

 # =====================
 #  PRUEBAS
 # =====================
if __name__ == "__main__":
    # print(mostrar_productos())

   print(buscar_producto_por_id(3))
    



