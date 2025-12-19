def gestionar_banca():
    saldo = 1000
    pin_correcto = "1234"

    pin_ingresado = input("Bienvenido al cajero automático, teclee su codigo PIN para continuar: ")
    if pin_ingresado != pin_correcto:
        print("PIN incorrecto. Acceso denegado.")
        return

    print("PIN correcto. Acceso concedido.")

    continuar = "si"

    while continuar.lower() == "si":

        print("\nSeleccione una opción:")
        print("1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            print(f"Su saldo actual es: {saldo} euros.")

        elif opcion == "2":
            cantidad = int(input("Teclee la cantidad a ingresar: "))

            if cantidad <= 0:
                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")
            else:
                saldo += cantidad
                print(f"Has ingresado {cantidad} euros. Su nuevo saldo es: {saldo} euros.")

        elif opcion == "3":
            cantidad = int(input("¿Qué cantidad desea retirar?: "))

            if cantidad <= 0:
                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")
            elif cantidad > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= cantidad
                print(f"Ha retirado {cantidad} euros. Su saldo actual es: {saldo} euros.")
        elif opcion == "4":
            print("Hasta pronto 👋")
            break

        else:
            print("Opción no válida.")

        continuar = input("\n¿Desea realizar otra consulta? (si/no): ")

        print("Gracias por usar el cajero automático, vuelva pronto.")


gestionar_banca()
        

        

        

        

      
