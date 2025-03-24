def calcular_descuento(monto_total_compra,porcentaje_descuento):   #funcion para calcular descuento
    descuento= (monto_total_compra*porcentaje_descuento)/100
    return descuento

def menu():         #funcion menu del sistema
    print("------Calculo de descuento a compras realizadas------")
    print("Elija una opcion:")
    print("1.-Carcular descuento")
    print("2.- Salir del sistema")

while True:
    menu()
    opcion= int(input("Ingrese la opcion a realizar:  "))

    if opcion == 2:
        print("Saliendo del sistema")
        break

    elif opcion == 1:
        monto= float(input("Precio original del producto:  "))    #ingreso del precio original

        descuento= float(input("Ingrese el porcentje de descuento:  "))  #ingreso del porcentaje de descuento
        cantidad_descuento = calcular_descuento(monto,descuento)         #llamar a la funcion
        print(f"La cantidad del descuento es: {cantidad_descuento}")    #cantidad de descuento
        total_pagar= monto-cantidad_descuento
        print(f"Precio final a pagar con descuento: {total_pagar}")     #precio final aplicado el descuento
    else:
        print("Opcion invalida")




    