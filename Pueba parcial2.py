# Programación de Algoritmos
# Profesor Giovanni Valdivia
# Prueba Parcial #2
#
# Autores: José Seguel : 14.255.183-7  ---  Angel Rojas : 19.837.745-7
#

# Constantes
tarifa_base = 500
costo_km = 100
costo_minuto = 20
dcto_frecuente = 0.1
dcto_aeropuerto = 0.2
total_acumulado = 0
viajes_realizados = 0


def pedir_opcion(max, min = 1, mensaje = None, error = None):
    if error == None:
        error = f"Debe ingresar un numero entre {min} y {max}."
    if mensaje == None:
        mensaje = "\n"
    correcto = False
    valor = None
    while not correcto:
        try:
            valor = int(input(mensaje))
            if valor >= min and valor <= max:
                correcto = True
            else:
                print(error)
        except:
            print("Debe ingresar un numero...")
    return valor

def pedir_numero(mensaje, min):
    error = f"Debe ingresar un numero mayor o igual a {min}"
    correcto = False
    valor = None
    while not correcto:
        try:
            valor = int(input(mensaje))
            if valor >= min:
                correcto = True
            else:
                print(error)
        except:
            print("Debe ingresar un numero...")
    return valor

def ingresar_viaje():
    # Datos iniciales
    origen = input("Ingrese punto de inicio: ")
    destino = input("Ingrese punto de destino: ")
    distancia = pedir_numero("Ingrese distancia recorrida: ", 0)
    espera = pedir_numero("Ingrese tiempo de espera: ", 0)
    
    # Descuentos
    porcentaje_dcto = 0.0
    frecuente = pedir_opcion(max=2, min=1, mensaje="Es usted cliente frecuente?\n1- Si\n2- No\n")
    aeropuerto = pedir_opcion(max=2, min=1, mensaje="Viaja al aeropuerto?\n1- Si\n2- No\n")
    if frecuente == 1:
        porcentaje_dcto += dcto_frecuente
    if aeropuerto == 1:
        porcentaje_dcto += dcto_aeropuerto
        
    # Calculo de costo
    sub_total = distancia*costo_km + espera*costo_minuto + tarifa_base
    descuento = int(round(porcentaje_dcto * sub_total))
    total = sub_total - descuento
    
    # Imprimir boleta
    print("\n\nViaje realizado!")
    print(f"Origen: {origen}    Destino: {destino}")
    print(f"Tarifa base: ${tarifa_base}")
    print(f"Distancia recorrida: {distancia}     Costo por Km: ${costo_km}")
    print(f"Tiempo de espera: {espera}     Costo por minuto de espera: ${costo_minuto}")
    print(f"Sub total: ${sub_total}")
    print(f"Descuentos: ${descuento}")
    print(f"Total: ${total}")
    print("Gracias por su viaje!\n\n")
    
    return total

def estadisticas_basicas():
    print(f"Total de viajes realizados: {viajes_realizados}")
    print(f"Total recaudado: ${total_acumulado}\n")

#funcion pasa salir del codigo
def salir():
    print("\nGracias por utilizar el sistema Rápido y Seguro")
    exit()

# Bucle principal
while True:
    print("---Bienvenido al sistema Rápido y Seguro---\n")
    print("             1- Ingresar viaje")
    print("              2- Estadisticas")
    print("                3- Salir\n")
    opcion = pedir_opcion(3, 1)
    if opcion == 1:
        total_acumulado += ingresar_viaje()
        viajes_realizados += 1
    elif opcion == 2:
        estadisticas_basicas()
    elif opcion == 3:
        break
    else:
        print("Error: Opcion ingresada invalida o no definida")

print("\nGracias por utilizar el sistema Rápido y Seguro")