#listaDeporte = []
NuevaListaDeporte = []
listaDeporte = ["Baseball", "Futbol", "Volley", "Natacion", "Futbol Americano"]
def obtenerListaDeportes():
    return ', '.join(map(str, listaDeporte))

def insertDepPosicion(deporte, posicion):
        posicion = int(posicion)
        listaDeporte.insert(posicion, deporte)
        return True
        
def agregarDeporteFinal(deporte):
      listaDeporte.append(deporte)
      return True

def eliminarDeporte(deporte):
    if deporte in listaDeporte:
        listaDeporte.remove(deporte)
        return True
    return False

def eliminarDeporteEspecifico(posicion):
     posicion = int(posicion)
     listaDeporte.pop(posicion)
     return True

def listaNuevosDeportes(deporte):
     NuevaListaDeporte.append(deporte)
     listaDeporte.extend(NuevaListaDeporte)
     return True

def clasificarDeportesOrden():
     listaDeporte.sort()
     return True

def clasificarDeportesReverso():
     listaDeporte.reverse()
     return True

def buscarDeporte(deporte):
    if deporte in  listaDeporte:
         listaDeporte.index(deporte)
         return True
    return False

def limpiarLista():
     listaDeporte.clear()
     return True