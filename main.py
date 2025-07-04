def add_task(task_name):
    # open JSON for writing
    # assign ID to task
    # store task and relevant details to JSON
    # output confirmation
    id = 1
    print("Task Added Successfully (ID: {id}, Name: {task_name})")


while True:
    command = input('task-cli:')
    operation, parameter = command.split(' ')
    match command:
        case "add":
            add_task(parameter)
        case "update":
            print("task update")
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
    