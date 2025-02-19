def rfc ():
    nombre = input("Introduzca su nombre:")
    fechaNac = input("Introduzca su fecha de nacimiento:")

    if len(fechaNac) != 6 or not fechaNac.isdigit():
        print("La fecha debe de tener exactamente 6 dígitos. Intente nuevamente")
        return None

    claveNombre = nombre.upper()[:4]

    rfc = (f"{claveNombre}{fechaNac}")
    return rfc

rfcGenerado = rfc()
if rfc:
    print("RFC: ", rfcGenerado)