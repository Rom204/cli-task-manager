import json
import inquirer


def load_tasks(f: str):
    try:    
        with open(f"{f}.json") as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        print("no tasks in this file yet")
        return []
    
def save_tasks(f: str, tasks):
    with open(f"{f}.json", "w") as file:
         json.dump(tasks, file)

def add_task(tasks):
    new_task = input("add a new task: ")
    tasks.append(new_task)
    print("task added successfuly")

def delete_task(tasks):
    view_task_list(tasks)
    target = int(input("type task number you would like to delete: "))
    tasks.pop(target - 1)
    print("task removed successfuly !")

def edit_task(tasks):
    view_task_list(tasks)
    target = int(input("type task number you would like to change: "))
    new_task = input("enter new task here: ")
    tasks[target - 1] = new_task
    print("task has been changed successfuly !")

def view_task_list(tasks):
    print("here are your current tasks !")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def exit(name: str, tasks):
    save_tasks(name, tasks)
    print("we saved your tasks, come back later if youd like to see them")


tasks_menu_dic = {
    "add": add_task,
    "delete": delete_task,
    "edit": edit_task,
    "view": view_task_list,
    "exit": exit
}

tasks_menu_question = [
    inquirer.List(
        "command",
        message="choose a command",
        choices=["add", "delete", "edit", "view", "exit"]
    )
]
def tasks_menu(f: str):
    tasks = load_tasks(f)

    while True:
        answer = inquirer.prompt(tasks_menu_question)
        if answer['command'] == "exit":
            exit(f, tasks)
            break
        else:
            tasks_menu_dic[answer['command']](tasks)
        
                