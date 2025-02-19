import re
import hashlib

def obtenerConsonante(palabra):
    for letra in palabra[1:]:
        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            return letra
    return "X"


def estadoClasificacion():
    clasificacion = {
        "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
        "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS", 
        "CHIHUAHUA": "CH", "CIUDAD DE MÉXICO": "DF", "DURANGO": "DG",
        "GUANAJUATO": "GT", "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC",
        "MÉXICO": "MC", "MICHOACÁN": "MN", "MORELOS": "MS", "NAYARIT": "NT",
        "NUEVO LEÓN": "NL", "OAXACA": "OC", "PUEBLA": "PL", "QUERÉTARO": "QT",
        "QUINTANA ROO": "QR", "SAN LUIS POTOSÍ": "SP", "SINALOA": "SL", 
        "SONORA": "SR", "TABASCO": "TC", "TAMAULIPAS": "TS", "TLAXCALA": "TL",
        "VERACRUZ": "VZ", "YUCATÁN": "YN", "ZACATECAS": "ZS", "NACIDO EN EL EXTRANJERO": "NE"
    }

    while True:
        estado = input("Estado de nacimiento: ").strip().upper()

        if estado in clasificacion:
            return clasificacion[estado]
        else:
            print("Estado inválido. Ingresa un estado válido (Ejemplo: Guanajuato, Jalisco, DF).")

def generarCurp():
    nombre = input("Nombre(s): ").strip().upper()
    apellidoPa = input("Apellido paterno: ").strip().upper()
    apellidoMa = input("Apellido materno: ").strip().upper()

    año = input("Año de nacimiento (YYYY): ").strip()
    if len(año) != 4 or not año.isdigit():
        print("El año debe de tener exactamente 4 dígitos. Intente nuevamente")
        return None
    
    mes = input("Mes de nacimiento (MM): ").strip().zfill(2)
    if len(mes) != 2 or not mes.isdigit():
        print("El mes debe de tener exactamente 2 dígitos. Intente nuevamente")
        return None
    
    dia = input("Día de nacimiento (DD): ").strip().zfill(2)
    if len(dia) != 2 or not dia.isdigit():
        print("El día debe de tener exactamente 2 dígitos. Intente nuevamente")
        return None
    
    sexo = input("Sexo (H/M): ").strip().upper()
    
    estado = estadoClasificacion() 

    if not apellidoMa:
        apellidoMa = "X"

    curp = (
        apellidoPa[:2] + apellidoMa[:1] + nombre[:1] +
        año[-2:] + mes + dia + sexo + estado[:2] +
        obtenerConsonante(apellidoPa) +
        obtenerConsonante(apellidoMa) +
        obtenerConsonante(nombre) + "00"
    )

    return curp.upper()

def validarCurp(curp):
    regex = r"^[A-Z]{4}[0-9]{6}[HM][A-Z]{2}[BCDFGHJKLMNPQRSTVWXYZ]{3}[0-9A-Z]{2}$"
    return bool(re.match(regex, curp))

def conversionHash(curp):
    curp = curp.strip().upper()
    hash = hashlib.sha256(curp.encode()).hexdigest()
    return hash

def datosCurp(curp):
    fechaNac = curp[4:10]
    sexo = curp[10]
    estado = curp[11:13]
    return fechaNac, sexo, estado

while True:
    print("\n--- Menú CURP ---")
    print("1. Generar CURP")
    print("2. Ingresar CURP")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        curp = generarCurp()
        print(f"\nCURP generado: {curp}")
    elif opcion == "2":
        curp = input("Ingresa un CURP: ").strip().upper()
        if validarCurp(curp):
            fechaNac, sexo, estado = datosCurp(curp)
            print(f"Fecha de nacimiento: {fechaNac}")
            print(f"Sexo: {'Hombre' if sexo == 'H' else 'Mujer'}")
            print(f"Estado: {estado}")
            hash = conversionHash(curp)
            print(f"Hash: {hash}")
        else:
            print("CURP inválido.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
