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
├─ mostrar_productos()
├─ registrar_producto()
├─ buscar_producto()
├─ actualizar_producto()
├─ eliminar_producto()
├─ reporte_productos_bajo_stock()
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
- Capa de servicios.
- Integración main.py. Prueba de flujo global.
- Refactorizar conexión global por funciones tipo conectar() y cerrar().
- Desarrollar el menú principal en `main.py`.
- Integrar las operaciones CRUD con la interfaz de usuario.
- Implementar validaciones básicas de entrada.
- Incorporar manejo de excepciones mediante `try-except-finally`.
- Evaluar el uso de transacciones explícitas (`BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`) para garantizar la consistencia de los datos.
- Implementar eliminación de productos con confirmación previa.
- Incorporar Colorama para mejorar la experiencia visual de la aplicación.

- Probar cada operación de capa de datos de manera aislada:
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
integrar al menú mediante capa de servicios
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
- registrar_producto() ✓
- actualizar_producto() ✓
- Capa de datos ✓
- Capa de servicios ✓
- Capa de aplicacion:
  - El esqueleto del Menú principal validado: ✔
    - Entrada no numérica ✔
    - Opción fuera de rango ✔
    - Opciones válidas ✔
    - Salida ✔
    - Captura de opción ✔
    - Validación de opción ✔
- Opción 1 (alta) ✔
    - Validación de nombre ✔
    - Validación de cantidad ✔
    - Validación de precio ✔
    - Persistencia en SQLite ✔
- Opción 2 (listado) ✔
- Flujo completo main → service → db → sqlite → db → service → main ✔
- Opcion 3 (busqueda por id) ✔
  - Validación de id ✔ 
  - id existente
  - id inexistente
- Opcion 4 (actualizacion por id)
  - ID existente → actualiza correctamente ✔
  - ID inexistente → informa y vuelve al menú ✔
  - Validaciones: ✔
     - 0        ✔
     - negativos✔
     - decimales✔
     - texto✔
     - Enter✔

## Modulos

#### Diseño de capas consistente
```
main.py               → presentación
inventario_service.py → lógica de negocio
inventario_db.py      → acceso a datos
inventario.db         → base de datos física
```
```
Ejemplo:

main.py
    ↓
registrar_producto(producto)
    ↓
inventario_service.py
    ↓
registrar_producto(producto)
    ↓
inventario_db.py
    ↓
cursor.execute('''INSERT INTO...''')
    ↓
inventario.db
```
### main.py

Punto de entrada de la aplicación. Interfaz de usuario. Gestiona el menú, la interacción con el usuario y las llamadas a las funciones del sistema.

##### Responsabilidades
- Mostrar el menú principal.
- Capturar la opción seleccionada.
- Validar la entrada del usuario.
- Mostrar alertas.
- Capturar los datos necesarios para cada operación.
- Invocar las funciones de inventario_service.py.
- Mostrar resultados y mensajes al usuario.

#### Flujo principal
```
main()
│
└─ while True ← menú principal
    │
    ├─ mostrar_menu()
    ├─ opcion = capturar_opcion()
    │
    └─ if opcion == 1
         │
         ├─ pedir nombre
         ├─ pedir descripción
         │
         ├─ while True       ← validar cantidad
         │    └─ try/except
         │
         ├─ while True       ← validar precio
         │    └─ try/except
         │
         ├─ pedir categoria
         ├─ construir diccionario
         └─ registrar_producto()
    ├─ elif opcion == 2
    │    ├─ mostrar_productos()
    │    └─ mostrar resultado
    │
    ├─ elif opcion == 3
    │    ├─ capturar id
    │    ├─ while True       ← validar id
    │    │    └─ try/except
    │    ├─ buscar_producto_por_id()
    │    └─ mostrar resultado
    │
    ├─ elif opcion == 4
        ├─ capturar id
        ├─ while True       ← validar id
    │   │    └─ try/except
        ├─ capturar nuevos datos
        ├─ validar nuevos datos
        ├─ construir producto
        ├─ actualizar_producto(id, producto)
        └─ mostrar resultadoo
    │
    ├─ elif opcion == 5
    │    ├─ capturar id
    │    ├─ eliminar_producto()
    │    └─ mostrar resultado
    │
    ├─ elif opcion == 6
    │    ├─ capturar cantidad
    │    ├─ reporte_productos_bajo_stock()
    │    └─ mostrar resultado
    │
    └─ elif opcion == 7
         └─ salir
```
##### Mejoras sugeridas

- Validación de datos al registrar un producto.
- El nombre no puede estar vacío.
- El precio debe ser un número mayor que cero.
- Eliminación de productos con confirmación previa.
- Integración de Colorama para mejorar la experiencia visual.
  - Mensajes de error y advertencia en rojo.
  - Confirmaciones en verde.
  - Información general en azul.
- Agregas un dato a cada producto que contenga la fecha y hora de la insercion, usando la librería datetime.
### inventario_service.py

- Capa de servicios
- Aporta seguridad
- Orquestación de las operaciones de inventario_db.py
- Funciones pasarela llaman a funciones de capa de datos
```
mostrar_productos()
↓
select_all()
```
```
registrar_producto(producto)
↓
registrar_producto(producto)
```
```
buscar_producto_por_id(id)
↓
buscar_producto_por_id(id)
```
```
actualizar_producto(id, producto)
↓
actualizar_producto(id, producto)
```
```
eliminar_producto(id)
↓
eliminar_producto_by_id(id)
```
```
reporte_productos_bajo_stock(cantidad)
↓
reporte_productos_bajo_stock(cantidad)
```

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
   registrar_producto()
actualizar_producto()
   reporte_productos_bajo_stock()

5. pruebas temporales
  - Inserciones iniciales: comentadas, para no duplicar datos.
  - SELECT: sin comentar.
  - UPDATE y DELETE: comentadas, porque modifican datos y no conviene repetirlas.
  - Bloque envuelto en if __name__ == "__main__": para que las pruebas no corran al importar el módulo.
   
  6. commit (dentro de pruebas temporales)
  7. close (dentro de pruebas temporales)
   ```