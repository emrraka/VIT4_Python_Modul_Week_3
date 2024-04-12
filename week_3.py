# Function to add a new task
def add_task(task_name, tasks):
    sequence_number = len(tasks) + 1
    new_task = {
        "Sequence Number": sequence_number,
        "Task Name": task_name,
        "Status": "Pending"
    }
    tasks.append(new_task)
    print("Task '{}' has been added with sequence number {}.".format(task_name, sequence_number))

# Function to complete a task
def complete_task(sequence_number, tasks):
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            task["Status"] = "Completed"
            print("Task '{}' marked as completed.".format(task["Task Name"]))
            return
    print("Task with sequence number {} not found.".format(sequence_number))

# Function to delete a task
def delete_task(sequence_number, tasks):
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            task["Status"] = "Deleted"
            print("Task '{}' deleted.".format(task["Task Name"]))
            return
    print("Task with sequence number {} not found.".format(sequence_number))

# Function to list completed tasks
def list_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task["Status"] == "Completed"]
    if completed_tasks:
        print("Completed tasks:")
        for task in completed_tasks:
            print("Sequence Number: {}, Task Name: {}".format(task["Sequence Number"], task["Task Name"]))
    else:
        print("No completed tasks.")

# Function to list all tasks with their status
def list_all_tasks(tasks):
    print("All tasks:")
    for task in tasks:
        print("Sequence Number: {}, Task Name: {}, Status: {}".format(task["Sequence Number"], task["Task Name"], task["Status"]))

# Main function
def main():
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. List completed tasks")
        print("5. List all tasks with their status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name, tasks)
        elif choice == "2":
            sequence_number = int(input("Enter sequence number of task to mark as completed: "))
            complete_task(sequence_number, tasks)
        elif choice == "3":
            sequence_number = int(input("Enter sequence number of task to delete: "))
            delete_task(sequence_number, tasks)
        elif choice == "4":
            list_completed_tasks(tasks)
        elif choice == "5":
            list_all_tasks(tasks)
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()