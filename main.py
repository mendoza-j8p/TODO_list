import os
import sys
from colorama import init, Fore, Style
from tasks.task_manager import create_task, show_tasks, update_task, delete_task
from utils.helpers import load_tasks

init(autoreset=True)

def main():
    tasks = load_tasks()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar terminal
        print(Style.BRIGHT + Fore.CYAN + f"===== TO-DO LIST ===== PYTHON VERSION: {sys.version.split()[0]}")
        print(Fore.CYAN + "1. Crear tarea")
        print(Fore.YELLOW + "2. Ver tareas")
        print(Fore.BLUE + "3. Actualizar tarea a completada")
        print(Fore.MAGENTA + "4. Eliminar tarea")
        print(Fore.RED + "5. Salir")
        print(Style.RESET_ALL)
        choice = input(Fore.WHITE + "Seleccione una opción >> ")

        if choice == '1':
            create_task(tasks)

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            print(Fore.BLUE + "Ingrese el nombre de la tarea a actualizar como completada: ")
            task_name = input()
            update_task(tasks, task_name)

        elif choice == '4':
            show_tasks(tasks)
            print(Fore.MAGENTA + "Ingrese el nombre de la tarea a eliminar, o escriba ALL para eliminar todas las tareas: ")
            task_name = input()
            delete_task(tasks, task_name)

        elif choice == '5':
            print(Fore.RED + "¡Hasta pronto!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
        input(Style.BRIGHT + Fore.YELLOW + "Presione Enter para continuar...")

if __name__ == "__main__":
    main()
