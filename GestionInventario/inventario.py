import pickle  # Importamos el módulo pickle para serializar y deserializar objetos


# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto. Inicializa un producto con su ID, nombre, cantidad y precio.

        Args:
        id (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible del producto.
        precio (float): Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener y establecer valores
    def obtener_id(self):
        """
        Devuelve el ID del producto.

        Returns:
        str: ID del producto.
        """
        return self.id

    def establecer_nombre(self, nombre):
        """
        Establece el nombre del producto.

        Args:
        nombre (str): Nuevo nombre del producto.
        """
        self.nombre = nombre

    def obtener_nombre(self):
        """
        Devuelve el nombre del producto.

        Returns:
        str: Nombre del producto.
        """
        return self.nombre

    def establecer_cantidad(self, cantidad):
        """
        Establece la cantidad del producto.

        Args:
        cantidad (int): Nueva cantidad del producto.
        """
        self.cantidad = cantidad

    def obtener_cantidad(self):
        """
        Devuelve la cantidad del producto.

        Returns:
        int: Cantidad del producto.
        """
        return self.cantidad

    def establecer_precio(self, precio):
        """
        Establece el precio del producto.

        Args:
        precio (float): Nuevo precio del producto.
        """
        self.precio = precio

    def obtener_precio(self):
        """
        Devuelve el precio del producto.

        Returns:
        float: Precio del producto.
        """
        return self.precio

    # Representación en cadena (útil para mostrar productos)
    def __str__(self):
        """
        Devuelve una representación en cadena del producto, mostrando su ID, nombre, cantidad y precio.

        Returns:
        str: Descripción del producto.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


# Clase que representa el inventario
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario. Inicializa un diccionario vacío para almacenar productos.
        """
        # Usamos un diccionario para almacenar productos con su ID como clave
        self.productos = {}

    # Método para añadir un nuevo producto
    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Args:
        producto (Producto): El producto a añadir.
        """
        self.productos[producto.obtener_id()] = producto

    # Método para eliminar un producto por ID
    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario utilizando su ID.

        Args:
        id (str): ID del producto a eliminar.
        """
        if id in self.productos:
            del self.productos[id]

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto existente en el inventario.

        Args:
        id (str): ID del producto a actualizar.
        cantidad (int, opcional): Nueva cantidad del producto. Si es None, no se actualiza.
        precio (float, opcional): Nuevo precio del producto. Si es None, no se actualiza.
        """
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id].establecer_precio(precio)

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        """
        Busca y devuelve una lista de productos que coincidan con el nombre dado.

        Args:
        nombre (str): Nombre del producto a buscar.

        Returns:
        list: Lista de productos que coinciden con el nombre.
        """
        return [producto for producto in self.productos.values() if producto.obtener_nombre() == nombre]

    # Método para mostrar todos los productos del inventario
    def mostrar_inventario(self):
        """
        Muestra todos los productos almacenados en el inventario.
        """
        for producto in self.productos.values():
            print(producto)

    # Método para guardar el inventario en un archivo
    def guardar_inventario(self, archivo):
        """
        Guarda el inventario en un archivo utilizando pickle para la serialización.

        Args:
        archivo (str): Nombre del archivo donde se guardará el inventario.
        """
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    # Método para cargar el inventario desde un archivo
    def cargar_inventario(self, archivo):
        """
        Carga el inventario desde un archivo utilizando pickle para la deserialización.
        Si el archivo no existe, se inicia un inventario vacío.

        Args:
        archivo (str): Nombre del archivo desde el cual se cargará el inventario.
        """
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado. Comenzando con un inventario vacío.")


# Función que implementa el menú interactivo
def menu():
    """
    Función principal que ejecuta el menú interactivo para gestionar el inventario.
    Permite al usuario añadir, eliminar, actualizar, buscar y mostrar productos,
    además de guardar y cargar el inventario desde un archivo.
    """
    inventario = Inventario()
    inventario.cargar_inventario("inventario.pkl")  # Cargar el inventario desde un archivo

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Añadir un nuevo producto al inventario
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")

        elif opcion == "2":
            # Eliminar un producto por ID
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado.")

        elif opcion == "3":
            # Actualizar la cantidad o el precio de un producto
            id = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad (deja en blanco para no cambiar): ") or -1)
            precio = float(input("Nuevo precio (deja en blanco para no cambiar): ") or -1)
            # Si el usuario deja en blanco el valor, no se actualizará el atributo respectivo
            inventario.actualizar_producto(id, cantidad if cantidad != -1 else None, precio if precio != -1 else None)
            print("Producto actualizado.")

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            # Mostrar todos los productos del inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Guardar el inventario en un archivo
            inventario.guardar_inventario("inventario.pkl")
            print("Inventario guardado.")

        elif opcion == "7":
            # Guardar el inventario y salir del programa
            inventario.guardar_inventario("inventario.pkl")
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elige nuevamente.")

# Punto de entrada principal
if __name__ == "__main__":
    menu()
