import os
import json
from datetime import datetime, timedelta


file_name = 'data.json'


def load_or_create_data_file():
    if os.path.exists(file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        print("""
              
              Welcome to SimpleTasks, my first python project.
              Feel free to report bugs to my github repository:
              https://github.com/
              
              Loaded existing user data.
              
              Press Control + C to exit.
              
              """)
        
    else:
        data = {"username": "", "to_do_list": []}
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("""
              
              Created new user data file.
              
              """)

    return data



def update_username(user_data, username):
    user_data["username"] = username
    

    with open(file_name, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)
    print("Username updated and saved.\n")
    
    
    

def display_tasks(user_data):
    if user_data["to_do_list"] == []:
        print("No tasks to display, so add some!\n")
    else:
        print("\nTodo List:\n")
        for index, task in enumerate(user_data["to_do_list"], start=1):
            print(f"{index}. {task['task']} (Due: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']})\n")



def add_task(user_data):
    task = input("\nEnter your task: ")
    priority = input("Enter your task priority (ex. Low, Medium, High): ")
    due_date_input = input("\nEnter the due date, or enter (24) to set it 24h from now: ")
    
    if due_date_input.lower() == '24':
        future_time = datetime.now() + timedelta(hours=24)
        due_date = future_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        due_date = due_date_input
    
    new_task = {
        "task": task,
        "priority": priority,
        'due_date': due_date,
        'status': "Incomplete"
    }
    
    user_data["to_do_list"].append(new_task)
    print("\nTask added successfully!\n")
    save_data_file(user_data)
    
    
    
def check_if_input_is_int(input_value):
    if isinstance(input_value, int):
        return True
    return False
    
    
    
    
def update_task(user_data):
    display_tasks(user_data)
    try:
        task_index = int(input("Enter the index of the task you want to update: ")) - 1
        if 0 <= task_index < len(user_data["to_do_list"]):
            task = user_data["to_do_list"][task_index]
            print(f"\nUpdating task: {task['task']}")
            
            completed_task = input("\nDo you want to mark the task as completed? (y), (n): ")
            
            if completed_task == "y":
                task["status"] = "Completed"
                print("\nTask updated successfully!\n")
                save_data_file(user_data)
            elif completed_task == "n":
                new_due_date = input("\nEnter the updated due date, or press (y) to keep the same: ")
                if new_due_date.lower() == 'y':
                    new_due_date = task["due_date"]
                    new_priority = input("\nEnter the new priority (ex. Low, Medium, High) or press (y) to keep the same: ")
                    if new_priority == "y":
                        print("\nKept the same priority.\n")
                        save_data_file(user_data)
                    else: 
                        task["priority"] = new_priority
                        print("\nPriority changed to {new_priority}\n")
                        save_data_file(user_data)
                task["due_date"] = new_due_date
                print("\nTask updated successfully!\n")
                save_data_file(user_data)
        else:
            print("Invalid task index.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        
        
        

def save_data_file(data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to JSON file.\n")
    
    

def delete_data_file(path):
    try:
        os.remove(path)
        print(f"File '{path}' deleted successfully, please restart your application.")
    except OSError as e:
        print(f"Error deleting the file: {e}")
    
    
    
    
def main():
    user_data = load_or_create_data_file()
    has_greeted = False

    try:
        while True:
            
            if has_greeted == False:
                if user_data["username"] == "":
                    username= input("What's your name?: ")
                    update_username(user_data, username)
                else: 
                    username = user_data["username"]
                    print(f"Welcome {username}\n")
                    has_greeted = True
                
            choice = input("Choose an option:\n\n1. Display tasks\n\n2. Add task\n\n3. Update task\n\n4. Delete your data file\n\nEnter your choice: ")

            if choice == "1":
                display_tasks(user_data)
            elif choice == "2":
                add_task(user_data)
            elif choice == "3":
                update_task(user_data)
            elif choice == "4":
                delete_data_file(file_name)
                break
            else:
                print("Invalid choice. Please select a valid option.\n")

    except KeyboardInterrupt:
        print("\nCtrl+C pressed. Exiting gracefully.\n")




if __name__ == "__main__":
    main()
