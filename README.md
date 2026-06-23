# Proyecto

Programa en **Python** desarrollado con fines educacionales que permite gestionar un inventario de productos mediante interfaz de consola. La aplicación implementa operaciones CRUD (alta, consulta, actualización y eliminación), búsqueda de productos por ID y generación de reportes de stock bajo. Integra SQLite3 para la persistencia de datos y se organiza mediante una arquitectura en capas compuesta por presentación (UI), servicios y acceso a datos.

## Estado del proyecto

Proyecto finalizado respecto de los requerimientos obligatorios.

Funcionalidades implementadas:

- Operaciones CRUD sobre productos.
- Búsqueda de productos por ID.
- Reporte de productos con bajo stock.
- Persistencia de datos mediante SQLite3.
- Interfaz de consola con Colorama.
- Arquitectura en capas (presentación, servicios y acceso a datos).
- Búsqueda de productos por nombre (implementada en capas de datos y servicios, pendiente integración en la interfaz, opcional segun la consigna).

---

## Requerimientos (consigna)

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

---

## Requisitos técnicos

El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.

Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.

---

## Arquitectura
```
main.py → inventario_service.py → inventario_db.py → inventario.db
```
### Mejoras arquitectónicas implementadas

- Inicialización explícita de la base de datos mediante init_db().
- Eliminación de efectos secundarios durante la importación del módulo.
- Gestión controlada de conexión y cursor SQLite.
- Cierre explícito de conexión mediante cerrar_conexion().
- Manejo de excepciones SQLite en la capa de presentación.
- Consistencia de nombres de variables y documentación.

### Funcionalidades opcionales 

- Búsqueda de productos por nombre implementada en las capas de acceso a datos y servicios. Pendiente integración en la interfaz de usuario. Pendiente implementación de búsqueda por categoría.

---

## Diseño conceptual

```
main.py
│
├─ menú
│   ├─ captura de opción
│   ├─ validaciones
│   └─ manejo de errores try/except
│
└─ llamadas a funciones de negocio

inventario_service.py
│
├─ inicializar()
├─ mostrar_productos()
├─ buscar_producto_por_id()
├─ buscar_productos_por_nombre()
├─ registrar_producto()
├─ actualizar_producto()
├─ eliminar_producto()
├─ reporte_productos_bajo_stock()
├─ cerrar()
│
└─ funciones pasarela hacia la capa de datos

inventario_db.py
│
├─ init_db()
│   ├─ conexión
│   ├─ cursor
│   └─CREATE TABLE productos
│
├─ select_all()
├─ buscar_producto_por_id()
├─ sselect_all_by_like_nombre()
│
├─ registrar_producto()
├─ actualizar_producto()
├─ eliminar_producto_by_id()
│
└─ reporte_productos_bajo_stock()

inventario.db
│
└─ persistencia de datos
```

---

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

Punto de entrada de la aplicación. Interfaz de usuario. Gestiona el menú, la interacción con el usuario y las llamadas a las funciones del sistema. Realiza validaciones y captura de excepciones.

##### Responsabilidades
- Mostrar el menú principal.
- Capturar la opción seleccionada.
- Validar la entrada del usuario.
- Mostrar alertas.
- Capturar los datos necesarios para cada operación.
- Invocar las funciones de inventario_service.py.
- Mostrar resultados y mensajes al usuario.
- Manejar excepciones.

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
- Funciones pasarela que delegan operaciones a la capa de acceso a datos y exponen servicios a la capa de presentación. Este diseño de arquitectura permite escalar la aplicación mediante la incorporación de reglas de negocio, validaciones centralizadas, auditoría, control de permisos o integración con otros sistemas sin afectar las demás capas. Estas capacidades no se encuentran implementadas en esta etapa.

```
Pasarela:

inventario_service.py
↓
inventario_db.py
```
Ejemplos
```
mostrar_productos()
↓
select_all()
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
   select_all_by_like_nombre()
   registrar_producto()
   actualizar_producto()
   eliminar_producto_by_id()
   reporte_productos_bajo_stock()
   ```

## Autor

Mariana Emilia Mazzoccoli (2026)