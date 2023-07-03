def calcular_precio(cantidad, precio_unitario):
    subtotal = cantidad * precio_unitario
    return subtotal

def menu_opciones():
    print("Bienvenido(a) a la cafetería")
    print("1. Espresso      $1.500")
    print("2. Capuchino     $1.800")
    print("3. Latte         $1.600")
    print("4. Moca          $1.700")
    print("0. imprimir boleta")
    opcion = input("Seleccione una opción del menú: ")
    return opcion

def realizar_pedido():
    total_pagar = 0
    productos = []
    while True:
        opcion = menu_opciones()
        if opcion == "1":
            cantidad = int(input("Ingrese la cantidad de Espresso que desea: "))
            subtotal = calcular_precio(cantidad, 1500)
            total_pagar += subtotal
            productos.append((cantidad, "Espresso", subtotal))
        elif opcion == "2":
            cantidad = int(input("Ingrese la cantidad de Capuchino que desea: "))
            subtotal = calcular_precio(cantidad, 1800)
            total_pagar += subtotal
            productos.append((cantidad, "Capuchino", subtotal))
        elif opcion == "3":
            cantidad = int(input("Ingrese la cantidad de Latte que desea: "))
            subtotal = calcular_precio(cantidad, 1600)
            total_pagar += subtotal
            productos.append((cantidad, "Latte", subtotal))
        elif opcion == "4":
            cantidad = int(input("Ingrese la cantidad de Moca que desea: "))
            subtotal = calcular_precio(cantidad, 1700)
            total_pagar += subtotal
            productos.append((cantidad, "Moca", subtotal))
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    descuento = 0
    if total_pagar >= 3000:
        descuento = total_pagar * 0.1
        total_pagar -= descuento

    # Imprimir la boleta
    print("******** BOLETA ********")
    for producto in productos:
        cantidad, nombre, subtotal = producto
        print(f"{nombre} x {cantidad}: ${subtotal}")
    print("------------------------")
    if descuento > 0:
        print(f"Descuento: ${descuento}")
    print("*******************************")
    print(f"Total a pagar: ${total_pagar}")

# Ejecutar el programa
realizar_pedido()