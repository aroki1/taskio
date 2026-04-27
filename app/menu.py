from app.errors import TaskError
from app.task_service import TaskService


class CLIMenu():
    def __init__(self, task_service: TaskService) -> None:
        self.task_service = task_service
            
    def print_menu(self) -> None:
        print()
        print("-" * 15)
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Update task title")
        print("5. Delete task")
        print("6. Exit")
        print("-" * 15)
        print()
    
    def get_task_id(self) -> int | None:
        try:
            return int(input("Enter task id: "))
        except ValueError:
            print()        
            print("Invalid task id. Please enter a number.")

    def get_user_option(self) -> int | None:
        try:
            return int(input("Enter your option: "))
        except ValueError:
            print(f"Invalid option. Please enter a number from 1 to 6.")

    def handle_add_task(self) -> None:
        task_title = str(input("Enter task title: "))
        self.task_service.add_task(task_title)

    def handle_list_tasks(self) -> None:
        print("*" * 15)
        tasks = self.task_service.list_tasks()
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\n\n".join(str(task) for task in tasks))
        print("*" * 15)

    def handle_complete_task(self) -> None:
        task_id = self.get_task_id()
        if task_id is None:
            return
        self.task_service.complete_task(task_id)
        print(f"Task #{task_id} marked as completed!")

    def handle_update_task_title(self) -> None:
        task_id = self.get_task_id()
        if task_id is None:
            return
        new_task_title = str(input("Enter new task title: "))
        self.task_service.update_task_title(task_id, new_task_title)
        print("Task successfully updated!")

    def handle_delete_task(self) -> None:
        task_id = self.get_task_id()
        if task_id is None:
            return
        
        self.task_service.delete_task(task_id)
        print("Task successfully deleted!")

    def run(self) -> None:
        print("Welcome to taskio!")
        while True:
            self.print_menu()
            user_option = self.get_user_option()
            if user_option is None:
                continue
            try:
                match user_option:
                    case 1:
                        self.handle_add_task()
                    case 2:
                        self.handle_list_tasks()
                    case 3:
                        self.handle_complete_task()
                    case 4:
                        self.handle_update_task_title()
                    case 5:
                        self.handle_delete_task()
                    case 6:
                        exit()
                    case _:
                        print()    
                        print(f"Invalid option. Please enter a number from 1 to 6.")
            except TaskError as err:
                print()
                print(err)