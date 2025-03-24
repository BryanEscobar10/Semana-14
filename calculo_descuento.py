def calcular_descuento(monto_total_compra,porcentaje_descuento):
    descuento= (monto_total_compra*porcentaje_descuento)/100
    return descuento

while True:
    print("------Calculo de descuento a compras realizadas------")
    print("Elija una opcion:")
    print("1.-Carcular descuento")
    print("2.- Salir del sistema")

    opcion= int(input("Ingrese la opcion a realizar:  "))

    if opcion == 2:
        print("Saliendo del sistema")
        break

    elif opcion == 1:
        monto= float(input("Precio original del producto:  "))
        descuento= float(input("Ingrese el porcentje de descuento:  "))
        cantidad_descuento = calcular_descuento(monto,descuento)
        print(f"La cantidad del descuento es: {cantidad_descuento}")
        total_pagar= monto-cantidad_descuento
        print(f"Precio final a pagar con descuento: {total_pagar}")
    else:
        print("Opcion invalida")




    