#listaCategorias = []
listaCategorias = ["HOGAR", "JARDINERIA"]
listaPendientes = []

def obtenerListaCategorias():
    return ', '.join(map(str, listaCategorias))

def añadirCategoria(categoria):
    opcion = categoria
    listaCategorias.append(opcion)
    return True

def insertarCategoria(posicion,categoria):
    posicion = int(posicion)
    listaCategorias.insert(posicion, categoria)
    return True

def renombrarCategoria(viejoNombre, nuevoNombre):
    if viejoNombre in listaCategorias:
        indice = listaCategorias.index(viejoNombre)
        listaCategorias[indice] = nuevoNombre
        return True
    return False
    
def clasificarCategoriaOrden():
     listaCategorias.sort()
     return True

def borrarCategoria(categoria):
    categoria = categoria
    if categoria in listaCategorias:
        listaCategorias.remove(categoria)
        return True
    return False

def seleccionarCategoriaParaPendientes(cat,actPendiente):
    if not listaCategorias:
        return "No hay categorías disponibles. Por favor, añade una categoría primero."
    
    print("\nCategorías disponibles:")
    for i, categoria in enumerate(listaCategorias, 1):
        print(f"{i}. {categoria}")
    
    try:
        
        if 1 <= range(cat) <= len(listaCategorias):
            categoriaSeleccionada = listaCategorias[cat - 1]
            listaPendientes.append({
                'categoria': categoriaSeleccionada,
                'actividad': actPendiente
            })
            return f"Actividad añadida exitosamente a la categoría {categoriaSeleccionada}"
        else:
            return "Número de categoría inválido"
    except ValueError:
        return "Por favor, ingresa un número válido"