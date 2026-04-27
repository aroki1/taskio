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
        
        task_id = 1
        if len(self.tasks) != 0:
            task_id = self.tasks[-1].id + 1
        
        task = Task(task_id, normalized_title, TaskStatus.IN_PROGRESS)
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

    def update_task_title(self, task_id: int, task_title: str) -> Task:
        normalized_title = task_title.strip()
        if normalized_title == "":
            raise TaskEmptyTitleError()
        
        if any(task.id != task_id and task.title == normalized_title for task in self.tasks):
            raise TaskAlreadyExistsError()
        
        for task in self.tasks:
            if task.id == task_id:
                task.title = normalized_title
                self.repository.save_tasks(self.tasks)
                return task
                
        raise TaskNotFoundError(task_id)
        
    def delete_task(self, task_id: int) -> Task:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                task = self.tasks.pop(i)
                self.repository.save_tasks(self.tasks)
                return task
            
        raise TaskNotFoundError(task_id)