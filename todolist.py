import os
import time

class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self):
      os.system('clear')
      do = input("Enter todo item: ")
      if do in self.tasks:
        print("Task already exists")
        input("Press enter to continue")
        self.add_task()
      elif do.lower()=="back":
        self.main()
      else:  
        self.tasks.append(do)
        a = input("Do you want to add more? (yes/no): ")
        if a.lower() == "yes":
            self.add_task()
        else:
            self.main()
   
    def main(self):
        os.system('clear')
        a = "\033[1m" + "Welcome to todo list".center(50) + "\033[0m"
        print(a)

        print("1. Add todo")
        print("2. Delete todo")  
        print("3. Update todo")  
        print("4. View todo")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.add_task()
        elif choice == 2:
            self.delete_task()
        elif choice == 3:
            self.update_task()
        elif choice == 4:
            self.view_tasks()
        elif choice == 5:
            print("Exiting...")
            time.sleep(2)
            for _ in range(5):  
                print(".", end="", flush=True)
                time.sleep(0.5)  
            return
        else:
            print("Invalid choice")

    def view_tasks(self):
        os.system('clear')
        print("Your To-Do list:")
        for index, task in enumerate(self.tasks, start=1):
            checkbox = "[ ]" if "[x]" not in task else ""  
            print(f"{index}. {task} {checkbox}")
        input("Press Enter to continue...")
        self.main()

    def delete_task(self):
        task_to_delete = input("Enter the task to delete: ")
        found = False
        for task_index, task in enumerate(self.tasks):
            if task == task_to_delete:
                self.tasks[task_index] = f"{task} [x]"  
                found = True
                print("Task deleted successfully!")
                break

        if not found:
            print("Task not found!")

        input("Press Enter to continue...")
        self.main()

    def update_task(self):
      b= input("Enter the task to update: ")
      if b in self.tasks:
        print("Task already exists")
        input("Press enter to continue")
        self.add_task()
      elif b.lower() ==  "back":
          self.main()
        
      else:  
        self.tasks.append(b)  
        input("Press Enter to continue...")
        self.main()

if __name__ == "__main__":
    todo_list = ToDo()
    todo_list.main()
