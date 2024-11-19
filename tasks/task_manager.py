from datetime import datetime
from colorama import Fore
from utils.helpers import save_tasks
from .task import Task

def create_task(tasks):
    while True:
        print(Fore.CYAN + "Ingrese el nombre de la tarea: ", end="")
        task_name = input()

        # Verificar si el usuario quiere salir
        if task_name.lower() == "exit":
            print(Fore.YELLOW + "Operación cancelada. Regresando al menú principal.")
            return
        # Verificar si se ingresó un nombre válido
        if task_name.strip():  # Si no está vacío o solo contiene espacios
            creation_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            task = Task(task_name)  # Crear tarea con nombre
            task.creation_datetime = creation_datetime  # Asignar fecha de creación
            tasks.append(task)
            save_tasks(tasks)
            print(Fore.GREEN + f"Tarea '{task_name}' creada exitosamente. Fecha de creación: {creation_datetime}")
            break
        print(Fore.RED + "El nombre de la tarea no puede estar vacío. Inténtalo de nuevo o escribe 'exit' para volver al menu.")

def show_tasks(tasks):
    if not tasks:
        print(Fore.RED + "<No hay tareas disponibles>")
    else:
        print(Fore.YELLOW + "Tareas:")
        for task in tasks:
            status = "Completada" if task.completed else "Pendiente"
            print(f"* {task.name} - {status} - Creada el: {task.creation_datetime}")
    print("\n")

def update_task(tasks, task_name):
    task_found = False  # Variable para verificar si la tarea fue encontrada
    for task in tasks:
        if task.name == task_name:
            task.completed = True
            print(Fore.GREEN + f"Tarea '{task_name}' marcada como completada.")
            task_found = True
            break  # Salir del bucle después de actualizar
    if not task_found:
        print(Fore.RED + f"Tarea '{task_name}' no encontrada.")

def delete_task(tasks, task_name):
    # Verificar si el usuario quiere eliminar todas las tareas
    if task_name.upper() == "ALL":
        confirmation = input(Fore.YELLOW + "¿Estás seguro de que quieres eliminar TODAS las tareas? (sí/no): ").strip().lower()
        if confirmation in ["sí", "si", "yes", "y"]:
            tasks.clear()  # Vaciar la lista de tareas
            print(Fore.GREEN + "¡Todas las tareas han sido eliminadas con éxito!")
        else:
            print(Fore.CYAN + "Operación cancelada. No se han eliminado tareas.")
        save_tasks(tasks)  # Guardar los cambios independientemente de la acción tomada
        return

    # Buscar y eliminar una tarea específica
    task_found = False
    for task in tasks:
        if task.name == task_name:
            tasks.remove(task)
            task_found = True
            print(Fore.GREEN + f"¡Tarea '{task_name}' eliminada con éxito!")
            break
    if not task_found:
        print(Fore.RED + f"Tarea '{task_name}' no encontrada.")
    save_tasks(tasks)
