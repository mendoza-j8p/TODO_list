import json
from tasks.task import Task

DATA_FILE = "tasks.json"

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks_data = json.load(file)
            tasks = [Task(name=task["name"],
                    completed=task.get("completed", False),
                    creation_datetime=task.get("creation_datetime", None)) for task in tasks_data]
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
