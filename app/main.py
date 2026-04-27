import argparse

from app.menu import CLIMenu
from app.task_repository import InMemoryRepository, JsonTaskRepository, TaskRepository
from app.task_service import TaskService
                
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to JSON file with tasks")
    args = parser.parse_args()    
    
    tasks_repo: TaskRepository = InMemoryRepository()
    if args.file:
        tasks_repo = JsonTaskRepository(args.file)
        
    task_service = TaskService(tasks_repo)
    cli_menu = CLIMenu(task_service)
    cli_menu.run()