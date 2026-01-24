from . import utils
from typing import Optional


class AsyncTodo:
    def __init__(self) -> None:
        self.path = "todo.json"
        self.todo: dict[str, str] = {}

    @classmethod
    async def create(cls):
        """Factory method"""
        instance = cls()
        instance.todo = await utils.load_file(instance.path)
        return instance

    async def add(self, item) -> str:

        if item in self.todo:
            return("Already Exists")
        else:
            self.todo[item] = "not Completed"
            await utils.write_to_file(self.path,self.todo)
            return "Item added"
        

    def get(self, item=None, getAll=False) -> str | list[str] | None:
        if len(self.todo) == 0:
            return "Empty todo"
        if getAll:
            return list(self.todo)
        if item is None:
            return "Item name required"
        if item not in self.todo:
            return "Item not Found"
        return self.todo[item]

    async def update(self, item, action) -> str | None:
        if item not in self.todo:
            shouldCreate = utils.parsed_input(
                "Item not found. You wanna create it? yes/no ", str
            )
            if shouldCreate == "yes":
                self.todo[item] = action
                await utils.write_to_file(self.path,self.todo)
                return "Item created"
            return "Item not created"

        self.todo[item] = action
        await utils.write_to_file(self.path,self.todo)
        return "Item Updated"

    async def delete(self, item) -> str | None:
        if item not in self.todo:
            return "Item Not found"
        self.todo.pop(item)
        await utils.write_to_file(self.path , self.todo)
        return "Item Deleted"
