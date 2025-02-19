from DevExamen import (obtenerListaCategorias, añadirCategoria, insertarCategoria,renombrarCategoria, clasificarCategoriaOrden,
                       borrarCategoria, seleccionarCategoriaParaPendientes)

while True:
    print("\n----Menú-----")

    print("1. Manipular Categoría.")
    print("2. Seleccionar una categoría y ver sus pendientes.")
    print("3. Salir del programa.")

    opciones = input("Seleccione una opción: ")

    if opciones == "1":
        while True:
            print("\n Gestión de Cateogorías.")
            print(obtenerListaCategorias())

            print("1. Dar de Alta categoría.")
            print("2. Insertar una categoría.")
            print("3. Renombrar Categoria.")
            print("4. Ordenar.")
            print("5. Borrar categoria.")

            op = input("Selecciona alguna opcion a realizar:")
        
            if op == "1":
                categoria = input("Introduzca una categoría:")
                if añadirCategoria(categoria):
                    print(f"Categoria añadida '{categoria}'")
                else:
                    print("Error, no se pudo mi pa")
            
            if op == "2":
                categoria = input("Inserte una categoria:")
                opcion = input("Insertar posición a insertar:")
                if insertarCategoria(opcion, categoria):
                    print(f"Categoria agregado en la posición '{opcion}'")
                else:
                    print("Error padrino")
            if op == "3":
                viejoNombre = input("Elija la categoria a renombrar:")
                nuevoNombre = input("Elija el nuevo nombre para la categoría:")
                if renombrarCategoria(viejoNombre, nuevoNombre):
                    print(f"La categoria cambio de nombre a '{nuevoNombre}'")
             
            if op == "4":
                if clasificarCategoriaOrden():
                       print("Lista ordenada alfabéticamente")
                else:
                       print("No se pudo ordenar jaja")
            if op == "5":
                categoria = input("Seleccione categoria a borrar:")
                if borrarCategoria(categoria):
                    print(f"Categoria borrada '{categoria}' ")
                else:
                    print("No se pudo borrar la categoria")
    elif opciones == "2":
        while True:
            print("\n Categorias")
            print(obtenerListaCategorias())

            print("1. Selecciona una Categoria para visualizar las actividades pendientes.")
            print("2. Selecciona una Categoria para añadir actividades pendientes.")
            print("3. Selecciona una Categoria para insertar actividades pendientes.")
            print("4. Selecciona una Categoria para renombrar actividades pendientes.")
            print("4. Ordenar actividades pendientes.")
            print("5. Borrar una actividad pendiente")

            option = input("Selecciona para visualizar actividades:")

            if option == "2":
                cat = input("Introduzca una categoría:")
                actPendiente = input("Introduzca una actividad pendiente: ")
                if seleccionarCategoriaParaPendientes(cat, actPendiente):
                    print(f"Actividad añadida '{actPendiente}'")
                else:
                    print("Error, no se pudo mi pa")
            
    elif opciones == "3":
        print("Saliendo....")
        break
    else:
        print("Opción no valida, intente de nuevo.")
    