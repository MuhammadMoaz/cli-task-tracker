import json
import shlex
import datetime

def init_json():
    dict = {
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
        # Get the number of tasks stored in the JSON 
        id = len(file_data["tasks"]) + 1
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

        # Get task and update description
        task_index = int(task_id) - 1
        file_data["tasks"][task_index]["description"] = new_desc

        file.seek(0)
        file.truncate()

        # Write updated task back to JSON file
        json.dump(file_data, file, indent=4)
    
def parse_input(user_input):
    command = shlex.split(user_input)

    match command[0]:
        case "add":
            if len(command) == 2:
                add_task(command[1])
            else:
                print("Invalid Input")
        case "update":
            if len(command) == 3:
                update_task(command[1], command[2])
            else:
                print("Invalid Input")
        case "delete":
            print("task deleted")
        case "mark-in-progress":
            print("task marked as in progress")
        case "mark-done":
            print("task marked as done")
        case "list":
            print("listing tasks")
        case "quit":
            print("quitting...")
            exit()

def main():
    init_json()
    
    while True:
        # Get input
        user_input = input('task-cli:')
        parse_input(user_input)

if __name__ == "__main__":
    main()