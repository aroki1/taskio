# API

from app.errors import TaskAlreadyExistsError, TaskEmptyTitleError, TaskNotFoundError
from app.models import Task, TaskStatus
from app.task_repository import TaskRepository

class TaskService():
    def __init__(self, repository: TaskRepository) -> None:
        self.tasks = repository.load_tasks()
        self.repository = repository
    
    def add_task(self, task_title: str) -> list[Task]:
        normalized_title = task_title.strip()
        if normalized_title == "":
            raise TaskEmptyTitleError()
        
        if any(task.title == normalized_title for task in self.tasks):
            raise TaskAlreadyExistsError()
        
        task = Task(len(self.tasks) + 1, normalized_title, TaskStatus.IN_PROGRESS)
        self.tasks.append(task)
        self.repository.save_tasks(self.tasks)
        
        return self.tasks
    
    def list_tasks(self) -> list[Task]:
        return self.tasks

    def complete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.status = TaskStatus.COMPLETED
                self.repository.save_tasks(self.tasks)
                return task
            
        raise TaskNotFoundError(task_id)
