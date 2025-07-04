import json
import re

def add_task(task_name):
    # open JSON for writing
    # assign ID to task
    # store task and relevant details to JSON
    # output confirmation
    id = 1
    print(f"Task Added Successfully (ID: {id}, Name: {task_name})")

def main():
    print("HI!")
    while True:
        # Get input
        command = input('task-cli:')
        # Get operation from input
        operation = command.split('"')
        print(operation)
        # Match command using regex
        match operation[0].strip():
            case "add":
                add_task(operation[1])
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

main()