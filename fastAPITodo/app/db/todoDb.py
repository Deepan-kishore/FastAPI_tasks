from app.db.utils import load_file, write_to_file
from datetime import datetime


class ApiResponse:
    """Helper class to create standardized responses"""
    @staticmethod
    def success(message: str, data=None):
        return {
            "success": True,
            "message": message,
            "data": data,
            "error": None
        }
    
    @staticmethod
    def error(message: str, error: str):
        return {
            "success": False,
            "message": message,
            "data": None,
            "error": error
        }


class Todo:
    def __init__(self):
        self.todo = {}
        self.path = ""
        return

    @classmethod
    async def TodoConstructor(cls):
        instance = cls()
        instance.path = "todo.json"
        # await load file
        todo = await load_file(instance.path)
        instance.todo = todo
        return instance

    async def createTodo(self, item):
        if item in self.todo:
            return ApiResponse.error(
                "Failed to create todo",
                f"Todo item '{item}' already exists"
            )
        current_time = datetime.now().isoformat()
        self.todo[item] = {
            "status": "incompleted",
            "created_at": current_time,
            "updated_at": current_time
        }
        # await write_to_file
        res = await write_to_file(self.path, self.todo)
        if res == "File Updated":
            return ApiResponse.success(
                f"Todo '{item}' created successfully",
                self.todo[item]
            )
        return ApiResponse.error(
            "Failed to create todo",
            f"Could not write to file: {res}"
        )

    def getTodo(self, item=None):
        try:
            if len(self.todo) == 0:
                return ApiResponse.error(
                    "No todos found",
                    "Todo list is empty"
                )
            if item is None:
                return ApiResponse.success(
                    "Todos retrieved successfully",
                    self.todo
                )
            if item not in self.todo:
                return ApiResponse.error(
                    "Todo not found",
                    f"Todo item '{item}' does not exist"
                )
            return ApiResponse.success(
                f"Todo '{item}' retrieved successfully",
                {item: self.todo[item]}
            )
        except Exception as e:
            return ApiResponse.error(
                "Error retrieving todos",
                str(e)
            )

    async def updateTodo(self, item, action):
        if item not in self.todo:
            return ApiResponse.error(
                "Failed to update todo",
                f"Todo item '{item}' does not exist"
            )
        current_time = datetime.now().isoformat()
        self.todo.update({item: {
            "status": action,
            "created_at": self.todo[item].get("created_at", current_time),
            "updated_at": current_time
        }})
        res = await write_to_file(self.path, self.todo)
        if res == "File Updated":
            return ApiResponse.success(
                f"Todo '{item}' updated successfully",
                self.todo[item]
            )
        return ApiResponse.error(
            "Failed to update todo",
            f"Could not write to file: {res}"
        )
    
    async def deleteTodo(self, item):
        if item not in self.todo:
            return ApiResponse.error(
                "Failed to delete todo",
                f"Todo item '{item}' does not exist"
            )
        deleted_item = self.todo.pop(item)
        res = await write_to_file(self.path, self.todo)
        if res == "File Updated":
            return ApiResponse.success(
                f"Todo '{item}' deleted successfully",
                deleted_item
            )
        return ApiResponse.error(
            "Failed to delete todo",
            f"Could not write to file: {res}"
        )


model = None
async def initialteTodo():
        global model
        model = await Todo.TodoConstructor()
        return model


__export__ = ["model"]
    
