def main():
    opcion = 0
    
    while opcion != 5:
        print("\n--- SISTEMA BANCARIO ---")
        print("1. Registrar / Iniciar Sesion")
        print("2. Ingresar Saldo")
        print("3. Retirar Dinero")
        print("4. Consultar Saldo")
        print("5. Salir")
        
        try:
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print("Por favor, ingresa un numero.")
            continue

        if opcion == 1:
            print("# Falta programar: Logica de Registro (Compañero A)")
        elif opcion == 2:
            print("# Falta programar: Ingresar saldo (Compañero B)")
        elif opcion == 3:
            print("# Falta programar: Retirar dinero (Compañero B)")
        elif opcion == 4:
            print("Tu saldo actual es: $1500")
            print("Saldo : Disponible")

        elif opcion == 5:
            print("Saliendo del sistema...")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()