import argparse

from app.errors import TaskError
from app.task_repository import InMemoryRepository, JsonTaskRepository, TaskRepository
from app.task_service import TaskService

def print_menu() -> None:
    print()
    print("-" * 15)
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Exit")
    print("-" * 15)
    print()

def run(task_service: TaskService) -> None:
    print("Welcome to taskio!")
    while True:
        print_menu()
        try:
            user_option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid option. Please enter a number from 1 to 4.")
            continue
        try:
            match user_option:
                case 1:
                    task_title = str(input("Enter task title: "))
                    task_service.add_task(task_title)
                case 2:
                    print("*" * 15)
                    tasks = task_service.list_tasks()
                    if len(tasks) == 0:
                        print("No tasks yet!")
                        return
                    print("\n\n".join(str(task) for task in tasks))
                    print("*" * 15)
                case 3:
                    try:
                        task_id = int(input("Enter task id: "))
                    except ValueError:
                        print()        
                        print("Invalid task id. Please enter a number.")
                        continue
                    task_service.complete_task(task_id)
                case 4:
                    exit()
                case _:
                    print()    
                    print("Invalid option. Please enter a number from 1 to 4.")
        except TaskError as err:
            print()
            print(err)
                
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to JSON file with tasks")
    args = parser.parse_args()    
    
    tasks_repo: TaskRepository = InMemoryRepository()
    if args.file:
        tasks_repo = JsonTaskRepository(args.file)
    
    task_service = TaskService(tasks_repo)
    
    run(task_service)