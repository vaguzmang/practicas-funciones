def crear_menu(num_opciones):
   
    print("\n--- MENÚ ---")
    
    for i in range(1, num_opciones + 1):
        print(f"{i}. Opción {i}")

    print(f"{num_opciones + 1}. Salir")

    # Capturar la elección del usuario
    eleccion = int(input("\nSeleccione una opción: "))
    while 1< eleccion > num_opciones+1:            
        eleccion = int(input("\nSeleccione una opción: "))
        if eleccion < 1: 
            if 1 <= eleccion <= num_opciones + 1:
                if eleccion == num_opciones + 1:
                    print("Saliendo del menú...")
                else:
                    print(f"Elegiste: Opción {eleccion}")
                return eleccion
            else:
                print("⚠️ Opción no válida, intente de nuevo.")
    

# Ejemplo de uso:
opcion = crear_menu(3) 

if opcion == 1:
    print("👉 Código de la opción 1")
elif opcion == 2:
    print("👉 Código de la opción 2")
elif opcion == 3:
    print("👉 Código de la opción 3")
elif opcion == 4:
    print("👋 Fin del programa")
    