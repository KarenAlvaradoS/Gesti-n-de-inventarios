import os
from Clase_Producto import Producto

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo."""
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
            return
        
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            print("El archivo de inventario no se encuentra.")
        except PermissionError:
            print("No tienes permiso para acceder al archivo de inventario.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(f"{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        except PermissionError:
            print("No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Ocurrió un error al escribir el archivo: {e}")

    def añadir_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        self.guardar_inventario()
        print(f"Producto con ID {id_producto} eliminado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")
