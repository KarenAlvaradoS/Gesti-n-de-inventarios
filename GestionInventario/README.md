# Sistema de Gestión de Inventario

Este proyecto es un sistema avanzado de gestión de inventarios implementado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite añadir, eliminar, actualizar y buscar productos en el inventario, además de guardar y cargar los datos desde un archivo.

## Estructura del Proyecto

- **Producto**: Clase que representa un producto en el inventario. Contiene atributos como ID, nombre, cantidad y precio.
- **Inventario**: Clase que gestiona los productos utilizando un diccionario para un acceso rápido a través del ID. Permite realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en los productos.
- **Almacenamiento en Archivos**: Se utiliza el módulo `pickle` para serializar el inventario y guardarlo en un archivo. También se puede cargar el inventario desde el archivo al iniciar el programa.

## Instrucciones de Uso

1. Al iniciar el programa, el inventario se cargará automáticamente desde el archivo `inventario.pkl`.
2. A través del menú interactivo, puedes realizar las siguientes acciones:
   - Añadir un nuevo producto.
   - Eliminar un producto por su ID.
   - Actualizar la cantidad o el precio de un producto.
   - Buscar productos por nombre.
   - Mostrar todos los productos del inventario.
   - Guardar el inventario en el archivo.

## Requisitos

- Python 3.x
- PyCharm (opcional, pero recomendado para desarrollo)

## Cómo Ejecutar

Para ejecutar el programa, simplemente corremos el archivo `inventario.py` en nuestro entorno Python.
