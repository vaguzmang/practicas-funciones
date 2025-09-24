import os
opcion=-1
TareasPendientes=[]
while opcion != 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BIENVENIDOS A LISTADO DE TAREAS PENDIENTES")
    print("1. Ver mis tareas pendientes")
    print("2. Crear una nueva tarea")
    print("3. Actualizar estado de una tarea")
    print("4. Eliminar una tarea")
    print("0. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                if len(TareasPendientes) == 0:
                    print("No hay tareas pendientes")
                    input("Presione una tecla para continuar")
                else:   
                    print(TareasPendientes)
            case 2:
                nueva=input("indica una nueva tarea")
                TareasPendientes.append(nueva)
                input("Presione una tecla para continuar")


            case 3: 
                pass

            case 4:
                for i,Tarea in enumerate(TareasPendientes,1):
                    #print(f"Tus tareas pendientes son : {TareasPendientes}")
                    print(f"{i}. {Tarea}")
                    Eliminar=(input("indica el numero de la tarea a eliminar"))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada no válida. Por favor, ingrese un número entero.")
        input()