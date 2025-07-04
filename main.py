def add_task():
    # open JSON for writing
    # assign ID to task
    # store task and relevant details to JSON
    # output confirmation
    print("Task Added Successfully (ID: {id})")


while True:
    input = input('task-cli:')
    command, parameter = input.split(' ')
    match command:
        case "add":
            add_task()
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
    