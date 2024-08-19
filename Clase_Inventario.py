class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        print(f"Producto con ID {id_producto} eliminado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
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
