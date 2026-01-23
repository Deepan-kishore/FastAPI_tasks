import os
import json

actions = {
    "notCompleted": "Not Completed",
    "Started": "Started",
    "completed": "completed",
}


class Todo:

    def __init__(self) -> None:
        self.todo: dict[str, str] = {}
        self.file_path = "todo_data.json"
        self.load_from_file()
        return

    def load_from_file(self) -> None:
        """Load todo from json file if it exists"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path) as file:
                    self.todo = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error while reading file, starting with empty list")
                self.todo = {}
        else:
            print("File does not exist, Attempting to create file")
            try:
                with open(self.file_path, "x") as file:
                    json.dump({}, file)
                    self.todo = json.load(file)
            except:
                print("Error while creating file")
            else:
                print("File created")

        return

    def save_to_file(self) -> None:
        """Save todo list to JSON file"""
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.todo, file, indent=2)
        except IOError:
            print("Error Saving file")

    def isNew(self, item, action, minCheck=False):
        isNew = True if not self.todo.get(item) else False

        if minCheck or not isNew:
            return isNew
        else:
            max_tries = 3
            tries = 0

            while tries < max_tries:
                agreedToAddNew_raw = input(
                    "This task is new. should I add it? yes or no ? "
                )
                try:
                    agreedToAddNew = agreedToAddNew_raw.lower()
                    if agreedToAddNew not in ["yes", "no"]:
                        raise ValueError
                except ValueError:
                    print("invalid argument: type only yes or no.")
                    continue
                else:
                    return (
                        self.add(item, action)
                        if agreedToAddNew == "yes"
                        else "New Item but Not Added"
                    )
        return

    def add(self, item, action=actions["notCompleted"]):
        isNew = self.isNew(item, None, True)
        if not isNew:
            return "Already present"
        self.todo[item] = action
        self.save_to_file()
        return "Item added successfully"

    def getAll(self) -> str | dict[str, str]:
        return self.todo

    def getOne(self, item) -> str:
        isNew = self.isNew(item, None, True)
        if isNew:
            return "item not present"
        else:
            return self.todo.get(item) or "item not present"

    def update(self, item, action) -> str:
        isNew = self.isNew(item, action)
        if not isNew:
            self.todo.update({item: action})
            self.save_to_file()
        return "Updated"

    def delete(self, item) -> str:
        isNew = self.isNew(item, None, True)
        if isNew:
            return "Item Not Present"
        self.todo.pop(item)
        self.save_to_file()
        return "Item deleted Successfully"


instance = Todo()
exit = False
while not exit:
    print("Welcome to TODO")
    print("==========================================")
    print("1. Add Todo")
    print("2. Delete Todo")
    print("3. Update Todo")
    print("4. Show All Todos")
    print("5. Get Specific Todo")
    print("6. Main Menu")
    print("7. Exit")
    print("==========================================")
    option = input("Enter your option in number only: ")
    try:
        optionParsed = int(option)
    except ValueError:
        print("Invalid option -> Enter your option in number only")
        continue
    else:
        if optionParsed == 7:
            break
        match optionParsed:
            case 1:
                item = input("Enter todo item name: ")
                res = instance.add(item)
                print(res)
                continue
            case 2:
                item = input("Enter todo item name to delete: ")
                res = instance.delete(item)
                print(res)
                continue
            case 3:
                item = input("Enter todo item name to update: ")
                action = input("What do you want to change it to? ")
                res = instance.update(item, action)
                print(res)
                continue
            case 4:
                items = instance.getAll()
                print(items)
                continue
            case 5:
                item = input("Enter todo item name to view: ")
                res = instance.getOne(item)
                print(res)
                continue
            case 6:
                continue
            case _:
                print("Invalid response, Try Again ;-)")
                continue
