import json
import shlex
import uuid

def add_task(task_name):
    # open JSON for writing
    # assign ID to task
    # store task and relevant details to JSON
    # output confirmation
    id = 1
    print(f"Task Added Successfully (ID: {id}, Name: {task_name})")
    id += 1

def parse_input(user_input):
    command = shlex.split(user_input)
    print(command)
    print(len(command))

    match command[0]:
        case "add":
            if len(command) == 2:
                add_task(command[1])
            else:
                print("Invalid Input")
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

def main():
    while True:
        # Get input
        user_input = input('task-cli:')
        parse_input(user_input)

main()