# Proyecto

Programa en **Python** desarrollado con fines educacionales que permite gestionar un inventario de productos mediante interfaz de consola. La aplicación implementa operaciones CRUD (alta, consulta, actualización y eliminación), búsqueda de productos por ID y generación de reportes de stock bajo. Integra SQLite3 para la persistencia de datos y se organiza mediante una arquitectura en capas compuesta por presentación (UI), servicios y acceso a datos.

## Estado del proyecto

Proyecto finalizado.

Funcionalidades implementadas:

- Operaciones CRUD sobre productos.
- Búsqueda de productos por ID.
- Reporte de productos con bajo stock.
- Persistencia de datos mediante SQLite3.
- Interfaz de consola con Colorama.
- Arquitectura en capas (presentación, servicios y acceso a datos).

## Requerimientos

### Base de datos
 Crear una base de datos llamada `inventario.db` para almacenar los datos de los productos. 

#### Tabla `productos` 

Debe contener las siguientes columnas:

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
main.py → inventario_service.py → inventario_db.py → inventario.db
```

## Diseño conceptual

```
main.py
│
├─ menú
│   ├─ captura de opción
│   └─ validación básica
│
└─ llamadas a funciones de negocio

inventario_service.py
│
├─ registrar_producto()
├─ mostrar_productos()
├─ buscar_producto_por_id()
├─ actualizar_producto()
├─ eliminar_producto()
├─ reporte_productos_bajo_stock()
│
└─ funciones pasarela hacia la capa de datos

inventario_db.py
│
├─ conexion
├─ cursor
├─ CREATE TABLE productos
│
├─ select_all()
├─ buscar_producto_por_id()
├─ select_price_by_id()              # spike
├─ select_price_by_like_nombre()     # spike
│
├─ registrar_producto()
├─ actualizar_producto()
├─ actualizar_precio_by_id()         # spike
├─ eliminar_producto_by_id()
│
└─ reporte_productos_bajo_stock()

inventario.db
│
└─ persistencia de datos
```
## Modulos

#### Diseño de capas consistente
```
main.py               → presentación
inventario_service.py → servicios / pasarela
inventario_db.py      → acceso a datos
inventario.db         → persistencia
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
    │    │
    │    ├─ pedir nombre
    │    ├─ pedir descripción
    │    │
    │    ├─ while True       ← validar cantidad
    │    │    └─ try/except
    │    │
    │    ├─ while True       ← validar precio
    │    │    └─ try/except
    │    │
    │    ├─ pedir categoria
    │    ├─ construir diccionario
    │    └─ registrar_producto()
    │
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
    │    ├─ capturar id
    │    ├─ while True       ← validar id
    │    │    └─ try/except
    │    ├─ capturar nuevos datos
    │    ├─ validar nuevos datos
    │    ├─ construir producto
    │    ├─ actualizar_producto(id, producto)
    │    └─ mostrar resultadoo
    │
    ├─ elif opcion == 5
    │    ├─ capturar id
    │    ├─ while True       ← validar id
    │    │    └─ try/except
    │    ├─ mostrar producto
    │    ├─ solicitar confirmacion s/n
    │    ├─ if/else
    │    │    ├─ eliminar_producto()
    │    │    ├─ cancelar
    │    └─ mostrar resultado
    │
    ├─ elif opcion == 6
    │    ├─ capturar límite de stock
    │    ├─ while True       ← validar límite
    │    │    └─ try/except
    │    ├─ reporte_productos_bajo_stock(limite)
    │    ├─ si existen productos
    │    │    └─ mostrar resultado
    │    └─ si no existen productos
    │         └─ mostrar mensaje informativo
    │
    └─ elif opcion == 7
         └─ salir
```
##### Mejoras implementadas

- Validación de datos al registrar un producto.
- El nombre no puede estar vacío.
- Eliminación de productos con confirmación previa.
- Integración de Colorama para mejorar la experiencia visual.
  - Mensajes de error y advertencia en rojo.
  - Confirmaciones en verde.
  - Información general en azul.

### inventario_service.py

- Capa de servicios
- Orquestación de las operaciones de inventario_db.py
- Funciones pasarela llaman a funciones de capa de datos

 En la versión actual del proyecto, la capa de servicios funciona como una pasarela entre la capa de presentación y la capa de acceso a datos. La arquitectura permite escalar la aplicación mediante la incorporación de reglas de negocio, validaciones centralizadas, auditoría, control de permisos o integración con otros sistemas sin afectar las demás capas. Estas capacidades no se encuentran implementadas en esta etapa.

```
Pasarela:

inventario_service.py
↓
inventario_db.py
```
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

4. Funciones de acceso a datos
   select_all()
   buscar_producto_por_id()
   select_price_by_id()
   select_price_by_like_nombre()
   registrar_producto()
   actualizar_producto()
   actualizar_precio_by_id()
   eliminar_producto_by_id()
   reporte_productos_bajo_stock()
   ```