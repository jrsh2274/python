
import re

#funcion que valida que se ingresen datos cnumericos para las coordenas del arreglo
def validar_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            entero = int(entrada)
            return entero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def validar_email(email):
    # Expresión regular para validar el formato del correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email)

#funcion que muestra lalos lotes disponibles
def mostrar_disponibilidad_lotes(lotes):
    print("Lotes Disponibles:")
    for fila in lotes:
        for lote in fila:
            if lote == 'X':
                print("[X]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

     

#funcion para desplegar el detalle del lote seleccionado
def mostrar_detalles_lote(lotes_seleccionados, lote_idx, detalles_lotes):
    lote = lotes_seleccionados[lote_idx]
    numero_lote = lote_idx + 1

    # Obtener los detalles del lote desde la lista de detalles_lotes
    detalles = detalles_lotes[lote_idx]
    tamaño_terreno = detalles['tamaño_terreno']
    precio = detalles['precio']

    print("Detalles del Lote Seleccionado:")
    print("Número de Lote:", numero_lote)
    print("Tamaño del Terreno:", tamaño_terreno, "m²")
    print("Precio:","$", precio)

# Detalle de lotes disponibles desde una lista
detalles_lotes = [
    {'tamaño_terreno': 500, 'precio': 10000000},
    {'tamaño_terreno': 600, 'precio': 20000000},
    {'tamaño_terreno': 450, 'precio': 15000000},
    {'tamaño_terreno': 1000, 'precio': 5000000},
    {'tamaño_terreno': 5000, 'precio': 10000000}]


lotes_seleccionados = [1, 2, 3, 4, 5]


#funcion para desplegar informacion de los clientes 
def mostrar_clientes(clientes):
    print("Clientes que han comprado un lote:")
    for cliente in clientes:
        print("RUT:", cliente[0])
        print("Nombre:", cliente[1])
        print("Teléfono:", cliente[2])
        print("Correo Electrónico:", cliente[3])
        print()
#funcion para ingresar y validar datos del cliente que selecciono un lote para comprar
def seleccionar_lote(lotes, lotes_seleccionados, clientes, detalles_lotes):
    rut = input("Ingrese su RUT: ")
    while not rut.isdigit() or len(rut) != 8:
        print("RUT inválido. Debe ser un número de 8 dígitos.")
        rut = input("Ingrese su RUT nuevamente: ")

    nombre = input("Ingrese su nombre completo: ")
    while not nombre.replace(" ", "").isalpha():
        print("Nombre inválido. Debe contener solo letras y espacios.")
        nombre = input("Ingrese su nombre completo nuevamente: ")

    telefono = input("Ingrese su teléfono: ")
    while not telefono.isdigit() or len(telefono) != 9:
        print("Teléfono inválido. Debe ser un número de 9 dígitos.")
        telefono = input("Ingrese su teléfono nuevamente: ")

    email = input("Ingrese su correo electrónico: ")
    while not validar_email(email):
        print("Correo electrónico inválido.")
        email = input("Ingrese su correo electrónico nuevamente: ")

    mostrar_disponibilidad_lotes(lotes)    

    fila = validar_entero("Ingrese la fila del lote: ")
    columna = validar_entero("Ingrese la columna del lote: ")

    if fila < 0 or fila >= len(lotes) or columna < 0 or columna >= len(lotes[0]):
        print("Coordenadas inválidas. Intente nuevamente.")
        return
#valida si el lote ya fue seleccionado del arreglo
    if lotes[fila][columna] == 'X':
        print("El lote seleccionado no está disponible. Por favor, elija otro.")
        return
#despliega datos del lote seleccionado
    lotes[fila][columna] = 'X'
    lote_seleccionado = (fila, columna)
    lotes_seleccionados.append(lote_seleccionado)
    clientes.append((rut, nombre, telefono, email))

    print("¡Lote seleccionado con éxito!")

    lote_idx = len(lotes_seleccionados) - 1
    mostrar_detalles_lote(lotes_seleccionados, lote_idx,detalles_lotes)
#funcion pasa slair del codigo
def salir():
    print("¡Gracias por usar LoteosDuoc!")
    exit()

#funcion para desplegar menu principal
def main():
    lotes = [[' ' for _ in range(5)] for _ in range(10)]
    lotes_seleccionados = []
    clientes = []

    while True:
        print("\n--- Menú de LoteosDuoc ---")
        print("*****************************")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver Clientes")
        print("5. Salir")
        opcion = input("Ingrese la opción deseada: ")
        print("*************************") 

        if opcion == '1':
            mostrar_disponibilidad_lotes(lotes)
        elif opcion == '2':
            seleccionar_lote(lotes, lotes_seleccionados, clientes,detalles_lotes)
        elif opcion == '3':
            if len(lotes_seleccionados) == 0:
                print("No ha seleccionado ningún lote.")
            else:
                lote_idx = validar_entero("Ingrese el número de lote seleccionado: ") - 1
                if lote_idx < 0 or lote_idx >= len(lotes_seleccionados):
                    print("Número de lote inválido.")
                else:
                    mostrar_detalles_lote(lotes_seleccionados, lote_idx,detalles_lotes)
        elif opcion == '4':
            mostrar_clientes(clientes)
        elif opcion == '5':
             salir()
             print("Opción inválida. Intente nuevamente.")

# verifica si el archivo actual está siendo ejecutado directamente como un programa independiente 
 
if __name__ == '__main__':
    main()
