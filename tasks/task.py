from datetime import datetime

class Task:
    def __init__(self, name, completed=False, creation_datetime=None):
        self.name = name
        self.completed = completed
        self.creation_datetime = creation_datetime or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "completed": self.completed,
            "creation_datetime": self.creation_datetime
        }

    def display_task(self):
        return f"{self.name} - {'Completed' if self.completed else 'Pending'}"
