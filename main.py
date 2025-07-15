import json
import shlex
import datetime

def init_json():
    dict = {
        "last_id": 0,
        "tasks": [

        ]
    }

    # Read JSON for writing
    with open("tasks.json", "w") as file:
        json.dump(dict, file, indent=4)

def generate_id():
    # Open JSNB for reading
    with open("tasks.json", "r") as file:
        # Read JSON
        file_data = json.load(file)

        # Increment last_id counter
        file_data["last_id"] += 1
        id = file_data["last_id"]

        with open("tasks.json", "w") as file:
            json.dump(file_data, file, indent=2)

        # Return id
        return id

def add_task(task_name):
    # Generate task ID
    task_id = generate_id()

    # Get current date and time
    datetime_now = datetime.datetime.now()
    
    # Convert to string
    created_at = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

    # Create dict of the task and it's properties
    task_dict = {
        "id": task_id,
        "description": task_name,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": created_at 
    }

    # Read JSON and store in dictionary
    with open("tasks.json", "r+") as file:
        file_data = json.load(file)
        # Add new data to dictionary
        file_data["tasks"].append(task_dict)
        file.seek(0)
        # Write updated JSON back to the JSON file
        json.dump(file_data, file, indent=4)

    # Output confirmation
    print(f"Task Added Successfully (ID: {task_id}, Name: {task_name})")

def update_task(task_id, new_desc):
    # Read JSON
    with open("tasks.json", "r+") as file:
        # Load JSON data
        file_data = json.load(file)

        # Find the task by task_id
        for task in file_data["tasks"]:
            if str(task["id"]) == str(task_id):
                # Update task description
                task["description"] = new_desc
                break

        file.seek(0)
        file.truncate()

        # Write updated task back to JSON file
        json.dump(file_data, file, indent=4)

def delete_task(task_id):
    # Read JSON
    with open("tasks.json", "r+") as file:
        # Load JSON data
        file_data =  json.load(file)

        # Find the task by task_id
        for task in file_data["tasks"]:
            if str(task["id"]) == str(task_id):
                # Delete task
                file_data["tasks"].remove(task) 
                break
       
        file.seek(0)
        file.truncate()

        # Write updated JSON back to file
        json.dump(file_data, file, indent=4)

def mark_task_in_progress(task_id):
    # Read JSON file
    with open("tasks.json", "r+") as file:
        # Load JSON data
        file_data = json.load(file)

        # Find the task by task_id
        for task in file_data["tasks"]:
            if str(task["id"]) == str(task_id):
                # Update task status
                task["status"] = "in-progress"
                break

        file.seek(0)
        file.truncate()

        # Write update JSON back to file
        json.dump(file_data, file, indent=4)

def mark_task_done(task_id):
    # Read JSON file
    with open("tasks.json", "r+") as file:
        # Load JSON data
        file_data = json.load(file)

        # Find the task by task_id
        for task in file_data["tasks"]:
            if str(task["id"]) == str(task_id):
                # Update task status
                task["status"] = "done"
                break

        file.seek(0)
        file.truncate()

        # Write update JSON back to file
        json.dump(file_data, file, indent=4)

def list_tasks(task_status=None):
    status_list = ["todo", "done", "in-progress"]
    output_list = []

    if (task_status) in status_list:
        # Read JSON file
        with open("tasks.json", "r+") as file:
            # Load JSON data
            file_data = json.load(file)

            # Find the task by task_status
            for task in file_data["tasks"]:
                if task["status"] == task_status:
                    # Store task in list
                    output_list.append(task["description"])
                else:
                    print(f"Task with status {task_status} not found.")
            
            print(output_list)
    
    elif task_status is None:
        # Read JSON file
        with open("tasks.json", "r+") as file:
            # Load JSON data
            file_data = json.load(file)

            # Find all tasks
            for task in file_data["tasks"]:
                output_list.append(task["description"])
            
            print(output_list)
    else:
        print(f"Invalid Status {task_status}")

def parse_input(user_input):
    command = shlex.split(user_input)

    match command[0]:
        case "add":
            if len(command) == 2:
                add_task(command[1])
        case "update":
            if len(command) == 3:
                update_task(command[1], command[2])
        case "delete":
            if len(command) == 2:
                delete_task(command[1])
        case "mark-in-progress":
            if len(command) == 2:
                mark_task_in_progress(command[1])
        case "mark-done":
            if len(command) == 2:
                mark_task_done(command[1])
        case "list":
            if len(command) == 1:
                list_tasks()
            if len(command) == 2:
                list_tasks(command[1])
        case "quit":
            print("quitting...")
            exit()
        case _:
            print("Invalid Input!")

def main():
    init_json()
    
    while True:
        # Get input
        user_input = input('task-cli:')
        parse_input(user_input)

if __name__ == "__main__":
    main()