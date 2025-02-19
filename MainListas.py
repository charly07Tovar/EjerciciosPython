from DevListas import (obtenerListaDeportes, insertDepPosicion,agregarDeporteFinal,eliminarDeporte,
                       eliminarDeporteEspecifico, listaNuevosDeportes, clasificarDeportesOrden,
                       clasificarDeportesReverso, buscarDeporte, limpiarLista)

while True:
    print("\n----Lista de Deportes-----")
    
    print(obtenerListaDeportes())

    print("1. Agregar deporte en posición.")
    print("2. Agregar deporte al final de la lista.")
    print("3. Eliminar deporte encontrado en la lista.")
    print("4. Eliminar deporte indicado en la lista.")
    print("5. Introducir nuevos deportes a la lista.")
    print("6. Clasificar deportes por orden alfabético")
    print("7. Clasificar deportes por orden alfabético alrevez")
    print("8. Buscar deporte en la lista.")
    print("9. Limpiar lista.")
    print("10. Salir del programa.")

    opciones = input("Seleccione una opción: ")

    if opciones == "1":
        deporte = input("Introduzca el nombre de deporte: ")
        posicion = input("Introduzca la posición en la que desea agregarlo: ")
        if insertDepPosicion(deporte, posicion):
            print("Deporte agregado exitosamente")
        else:
            print("Error: posición inválida")
        
    elif opciones == "2":
        deporte = input("Introduzca el nuevo nombre del deporte a agregar: ")
        if agregarDeporteFinal(deporte):
            print("Deporte agregado: "+deporte)
        else:
            print("Deporte no agregado")
    elif opciones == "3":
        deporte=input("Introduzca el nombre del deporte a eliminar: ")
        if eliminarDeporte(deporte):
            print("Se ha eliminado: "+deporte)
        else:
            print("No se elimino el deporte")
    elif opciones == "4":
        op=input("Introduzca la posición del deporte a eliminar:")
        if eliminarDeporteEspecifico(op):
            print("Se ha eliminado por posición")
        else:
            print("No se pudo eliminar por posición")
    elif opciones == "5":
        deportes=input("Introduzca los nombres de los deportes a introducir en la lista:")
        if listaNuevosDeportes(deportes):
            print("Se han agregado los deportes a la lista")
        else:
            print("No se pudo agregar los deportes")
    elif opciones == "6":
        if clasificarDeportesOrden():
            print("Lista ordenada alfabéticamente")
        else:
            print("No se pudo ordenar la lista")
    elif opciones == "7":
        if clasificarDeportesReverso():
            print("Lista ordenada alrevez")
        else:
            print("No se pudo ordenar la lista")
    elif opciones == "8":
        deporte = input("Introduzca el nombre del deporte a buscar:")
        if buscarDeporte(deporte):
            print("El deporte está en la lista")
        else:
            print("No sepudo encontrar el deporte en la lista")
    elif opciones == "9":
        if limpiarLista():
            print("La lista ha sido limpiada")
        
    elif opciones == "10":
        print("Saliendo....")
        break
    else:
        print("Opción no valida, intente de nuevo.")