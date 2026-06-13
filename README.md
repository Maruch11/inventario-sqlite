# Proyecto

Desarrollar un programa en **Python** que cumpla con las siguientes características:

## Requerimientos

### Base de datos
 Crear una base de datos llamada `inventario.db` para almacenar los datos de los productos. 

#### La tabla `productos` debe contener las siguientes columnas:

- `id`: Identificador único del producto (clave primaria, autoincremental).
- `nombre`: Nombre del producto (texto, no nulo).
- `descripcion`: Breve descripción del producto (texto).
- `cantidad`: Cantidad disponible del producto (entero, no nulo).
- `precio`: Precio del producto (real, no nulo).
- `categoria`: Categoría a la que pertenece el producto (texto).

### Funcionalidades de la aplicación

La aplicación debe permitir:

- Registrar nuevos productos.
- Visualizar datos de los productos registrados.
- Actualizar datos de productos, mediante su ID.
- Eliminación de productos, mediante su ID.
- Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
- Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario.

### Interfaz de usuario

Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal. La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.

Opcional: Utilizar el módulo `colorama` para mejorar la legibilidad y experiencia de usuario en la terminal, añadiendo colores a los mensajes y opciones


## Requisitos técnicos

El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.

Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.

## Arquitectura
```
Solicitud       Respuesta

Usuario         inventario.db
  │                 │
  ▼                 ▼
main.py           inventario_db.py
  │                 │
  ▼                 ▼
inventario_service.py inventario_service.py
  │                 │
  ▼                 ▼
inventario_db.py main.py
  │                 │
  ▼                 ▼
inventario.db    Usuario
```
## Diseño conceptual

```
main.py
│
├─ conexion = conectar()
├─ crear_tabla(conexion)
│
├─ menú
│   ├─ captura de opción
│   └─ validación básica
│
└─ llamadas a funciones de negocio

inventario_service.py
│
├─ registrar_producto()
├─ buscar_producto()
├─ actualizar_producto()
├─ eliminar_producto()
├─ reporte_stock()
└─ orquestación de reglas de negocio

inventario_db.py
|
├─ conexion
├─ cursor
├─ CREATE TABLE productos
├─ select_all()
├─ buscar_producto_por_id()
├─ select_price_by_id()
├─ select_price_by_like_nombre()
├─ actualizar_precio_by_id()
├─ eliminar_producto_by_id()
└─ reporte_productos_bajo_stock()

inventario.db
│
└─ persistencia de datos
```
## Backlog técnico

- Crear la base `inventario.db`.
- Crear la tabla `productos`.
- Verificar conexión.
- Probar un `INSERT`.
- Probar un `SELECT`.
- Probar un `UPDATE`.
- Probar un `DELETE`.
- Reporte de productos cuya cantidad sea <= a un límite indicado por el usuario.
- Integración main.py
- Refactorizar conexión global por funciones tipo conectar() y cerrar().
- Desarrollar `menu`

Justificación técnica: el menú suele consumir menos tiempo que verificación de que las operaciones sobre la base funcionen correctamente.

- Probar cada operación de manera aislada
```
crear tabla
↓
insertar
↓
consultar
↓
actualizar
↓
eliminar
↓
buscar
↓
reporte
↓
integrar al menú
```

#### Checks
- CREATE TABLE ✓ 
- INSERT ✓
- SELECT ✓
- COMMIT ✓
- CLOSE ✓
- buscar precio por nombre con LIKE ✓ (spike técnico)
- buscar precio por id ✓ (spike técnico)
- Buscar producto por ID ✓ (SELECT FROM WHERE)
- Actualizar información de productos existentes ✓  (UPDATE SET WHERE)
- DELETE ✓
- Reporte de productos cantidad igual o inferior a un límite especificado ✓

## Modulos

### main.py

### inventario_service.py

### inventario_db.py
```
1. imports

2. conexión
   cursor

3. CREATE TABLE

4. funciones CRUD
   select_all()
   buscar_producto_por_id()
   select_price_by_id()
   select_price_by_like_nombre()
   actualizar_precio_by_id()
   eliminar_producto_by_id()
   reporte_productos_bajo_stock()

5. pruebas temporales
  - Inserciones iniciales: comentadas, para no duplicar datos.
  - SELECT: sin comentar.
  - UPDATE y DELETE: comentadas, porque modifican datos y no conviene repetirlas.
  - Bloque envuelto en if __name__ == "__main__": para que las pruebas no corran al importar el módulo.
   
  6. commit (dentro de pruebas temporales)
  7. close (dentro de pruebas temporales)
   ```
