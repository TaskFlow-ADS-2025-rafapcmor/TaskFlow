class Task:
    def __init__(self, title, description="", status="pendente"):
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status


class TaskFlow:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def remove_task(self, title):
        task = self.get_task(title)
        if task:
            self.tasks.remove(task)
            return True
        return False

