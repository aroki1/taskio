from pathlib import Path

import pytest

from app.errors import TaskEmptyTitleError, TaskNotFoundError
from app.task_repository import InMemoryRepository, JsonTaskRepository
from app.task_service import TaskService, Task

def setup_test_service() -> TaskService:
    repo = InMemoryRepository()
    task_service = TaskService(repo)
    return task_service

def test_create_task_with_default_status():
    task = Task(id=1, title="Learn python")
    assert task.id == 1
    assert task.title == "Learn python"
    assert task.status == "in-progress"

# add task
def test_add_task():
    task_service = setup_test_service()
    expected_task = Task(1, "Learn python", "in-progress")
    assert task_service.add_task("Learn python") == [expected_task]
    
def test_add_task_with_empty_title():
    task_service = setup_test_service()
    with pytest.raises(TaskEmptyTitleError):
        task_service.add_task("")

# complete task
def test_complete_task():
    task_service = setup_test_service()
    task_service.add_task("Learn python")
    task_service.add_task("Learn code")
    
    test_task = task_service.complete_task(1)
    expected_task = Task(1, "Learn python", "completed")
    
    assert test_task == expected_task

def test_complete_task_with_incorrect_id():
    task_service = setup_test_service()
    task_service.add_task("Learn python")
    task_service.add_task("Learn code")
    
    with pytest.raises(TaskNotFoundError):
        task_service.complete_task(100000)

# save and load tasks
def test_save_and_load_tasks_in_memory(tmp_path: Path):
    
    tasks = [
        Task(1, "Learn python", "in-progress"),
        Task(2, "Learn code", "in-progress")
    ]
        
    repo = InMemoryRepository()
    
    repo.save_tasks(tasks)
    loaded_tasks = repo.load_tasks()
    assert tasks == loaded_tasks

def test_save_and_load_tasks_json(tmp_path: Path):
    path = tmp_path / "tasks.json"
    
    tasks = [
        Task(1, "Learn python", "in-progress"),
        Task(2, "Learn code", "in-progress")
    ]
        
    repo = JsonTaskRepository(str(path))
    
    repo.save_tasks(tasks)
    loaded_tasks = repo.load_tasks()
    assert tasks == loaded_tasks    