#Modulos de menu: Usuario, Inventario con submodulos de agregar, quitar items y modificar producto (cantidad, nombre y precio), facturacion 
usuario = "admin"
contraseña = "12345"
auth = False

inventario = [
    ["Guitarra Acustica", 2, 20],
    ["Guitarra Electroacustica", 5, 30],
    ["Guitarra Electrica", 4, 40],
    ["Violin", 4, 75],
    ["Bajo", 15, 100],
    ["Requinto", 22, 55],
    ["Saxofon", 9, 30],
    ["Acordeon", 17, 90],
    ["Armónica", 8, 45],
    ["Flauta", 12, 75],
    ["Trompeta", 5, 60],
    ["Clarinete", 11, 85],
    ["Batería", 6, 20],
    ["Bongoe", 13, 65],
    ["Caja Vallenata", 21, 50],
    ["Piano de Cola", 19, 80],
    ["Piano Clavinova", 8, 30],
    ["Teclado de Estudio", 25, 75],
    ["Amplificadores", 14, 95],
    ["Audífonos", 18, 45],
    ["Mezcladores", 7, 35],
    ["Cabina", 0, 80],
    ["Interfaz", 9, 25]
]

def mostrar_inventario():
    print("\n")
    for articulo in inventario:
        print(f"{articulo[0]}, Cantidad: {articulo[1]}, Precio: {articulo[2]}")
    print("\n")


def agregar_articulo():
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad de artículos: "))
    precio = int(input("Precio del artículo: "))
    inventario.append([nombre, cantidad, precio])
    print(f"Artículo '{nombre}' agregado al inventario.\n")
    mostrar_inventario()


def modificar_articulo():
    mostrar_inventario()
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad de artículos: "))
    precio = int(input("Precio del artículo: "))
    for articulo in inventario:
        if articulo[0] == nombre:
            articulo[1] = cantidad
            articulo[2] = precio
            print(f"Artículo '{nombre}' modificado.\n")
            mostrar_inventario()
            return
    print(f"Artículo '{nombre}' no encontrado en el inventario.\n")


def eliminar_articulo():
    mostrar_inventario()
    nombre = input("Nombre del artículo: ")
    existente = False
    
    instrumento = 0
    while instrumento < len(inventario):
        articulo = inventario[instrumento]
        
        if articulo[0] == nombre:
            existente = True
            inventario.pop(instrumento)
            print(f"\n**Se ha eliminado '{nombre}' del inventario.**\n")
            mostrar_inventario()
            return  # Sale de la función después de eliminar el artículo
        
        instrumento += 1
    
    if not existente:
        print("\n**Producto no encontrado en inventario, ingrese de nuevo**\n")


def autenticacion ():
    usuario_input = input("Ingresar Usuario: ")
    contraseña_input = input("Ingresar Contraseña: ")
    if usuario == usuario_input and contraseña == contraseña_input:
        print("Inicio de sesion exitoso.")
        global auth
        auth = True
    else:
        print("Usuario o contraseña incorrectos, ingrese de nuevo.")
        

def ventas():
    mostrar_inventario()
    
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad de artículos: "))
    existente = False
    for item in inventario:

        if item[0] == nombre:
            existente = True

            if item[1] >= cantidad:

                item[1] -= cantidad

                total_venta = cantidad * item[2]
                print(f"Se vendieron {cantidad} {nombre}(s).")
                print(f"El total de la venta es: {total_venta} \n")
                menu ()
            
            else:
                print("\n **No hay suficiente cantidad en inventario o no existe, ingrese de nuevo.** \n")
                ventas()

    if existente == False:
        print("\n **Producto no encontrado en inventario, ingrese de nuevo** \n")
        ventas()
    

#MENU
def menu ():
    while auth == False:
        autenticacion()

    while True:
        
        print("***************************************************")
        print()
        print("           ****Bienvenido a PandaMusic!****           ")
        print()
        print("\t1 - Ventas")
        print("\t2 - Inventario")
        print("\t3 - Salir")
        print()
        print("***************************************************")
        
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            ventas()

        elif opcion == "2":
            print("***************************************************")
            print()
            print("           ****Inventario****           ")
            print()
            print("\t1 - Agregar articulo(s)")
            print("\t2 - Eliminar articulo(s)")
            print("\t3 - Mostrar inventario")
            print("\t4 - Modificar artículo")
            print("\t5 - Volver")
            print()
            print("***************************************************")
            
            opcion_inv = input("Ingrese la opción deseada: ")

            if opcion_inv == "1":
                agregar_articulo()

            elif opcion_inv == "2":
                eliminar_articulo()

            elif opcion_inv == "3":
                mostrar_inventario()

            elif opcion_inv == "4":
                modificar_articulo()

            elif opcion_inv == "5":
                menu ()

            else:
                print("**Opcion invalida, intentelo de nuevo.** \n\n\n")
                continue
                
        elif opcion == "3":
            print("Adios")
            break

        else:
            print("**Opcion invalida, intentelo de nuevo.** \n\n\n")
            menu ()


menu()
        

   
    
