import os

tasks = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...")

def menu():
    print("Bienvenido al sistema de gestión de tareas.")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Actualizar tarea")
    print("5. Salir")
    choice = input("Seleccione una opción: ")
    return choice

def add_task():
    task = input("Ingrese la tarea: ")
    tasks.append(task)
    print("Tarea agregada.")

def view_tasks():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task():
    task_num = int(input("Ingrese el número de la tarea a eliminar: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Tarea eliminada.")
    else:
        print("Número de tarea inválido.")

def exit_program():
    print("Saliendo del programa. ¡Hasta luego!")
    return False
    
def Actualizar(i):
        i=input("indique la tarea que desea actualizar")
        nueva=input("indique su actualizacion")
        nueva=tasks.pop(i-1)
        tasks.insert(i-1,nueva)
        return "Su tarea ha sido actualizada"


def main():
    isActive = True
    while isActive:
        clear_screen()
        choice = menu()
        if choice == '1':
            add_task()
            input()
        elif choice == '2':
            view_tasks()
            input()
            
        elif choice == '3':
            view_tasks()
            delete_task()
            input()
            
        elif choice == '4':
            view_tasks()
            i=input("indique la tarea que desea actualizar")
            nueva=input("indique su actualizacion")
            nueva=tasks.pop(i-1)
            tasks.insert(i-1,nueva)
            input()

        elif choice == '5':
            isActive = exit_program()
        else:
            print("Opción inválida. Intente de nuevo.")
            pause()

if __name__ == "__main__":
    main()