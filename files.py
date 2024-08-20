import inquirer 
from pathlib import Path
from tasks import tasks_menu


def is_files_exists():
    dir = Path('.')
    files_list = list(dir.glob('**/*.json'))
    if len(files_list) == 0:
            return False
    return files_list

def view_files():
    fs = is_files_exists()
    if fs:
        for i, file in enumerate(fs):
            print(f"{i + 1}. {file} \n")

def open_file():
    while True:
        f = input("enter a file to open from the list: ")
        try:
            with open (f + ".json", "r"):
                print(f"File {f}.json is now open!")

            tasks_menu(f)
            break
        except FileNotFoundError:
            print(f"File '{f}.json' doesnt exists")
            
def create_file():
    while True:
        f = input("enter new file name: ")
        try:
            with open(f + ".json", "x"):
                print(f"New file:  {f}.json was created !")
            break
        except FileExistsError:
            print(f"File '{f}.json' already exists.")

def update_file_name():
    # if the new path name is changed to an existing one, it will override it !!! therefore - need to check for availabilty first somehow.
    while True:
        f = input("enter file name you would like to change: ")
        try:
            p = Path(f + ".json")
            new_p = input("enter new file name: ")
            p.rename(new_p + ".json")
            print(f"File {f}.json has change to {new_p}.json")
            break
        except FileNotFoundError:
            print(f"File '{f}.json' does not exists")
        
def delete_file():
    while True:
        f = input("enter file name to delete: ")
        try:
            p = Path(f + ".json")
            p.unlink()
            print(f"File {f}.json has been deleted")
            break
        except FileNotFoundError:
            print(f"File '{f}.json' doesnt exists")

files_menu_dic = {
    "open" : open_file,
    "create" : create_file,
    "edit" : update_file_name,
    "view" : view_files,
    "delete" : delete_file,
    "exit" : "exit"
}

files_menu_question = [
    inquirer.List(
        "command",
        message="choose a command",
        choices=["open", "create", "edit", "view", "delete", "exit"],
    ),
]


def files_menu():

    while True:
        is_file_exists = is_files_exists()
        answer = inquirer.prompt(files_menu_question)
        if answer["command"] == "exit":
            break
        elif not is_file_exists and answer["command"] != "create":
            print("It seems you dont have any files yet, lets create one by typing 'cf' command !\n")
            continue
        else:
            files_menu_dic[answer["command"]]()
       