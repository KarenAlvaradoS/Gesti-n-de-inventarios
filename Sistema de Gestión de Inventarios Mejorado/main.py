from Clase_Producto import Producto
from Inventario import Inventario

def main():
    inventario = Inventario()

    while True:
        print("\nMenú de Inventario")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        
        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        
        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        
        elif opcion == '5':
            inventario.mostrar_todos()
        
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
