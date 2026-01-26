from fastapi import APIRouter
from typing import List
from app.schemas.todo_schema import TodoCreate, TodoUpdate, ApiResponse
import app.db.todoDb as todoDb


todoRouter = APIRouter()

@todoRouter.get('/get', response_model=ApiResponse)
async def get_all():
    res = todoDb.model.getTodo(item=None)
    return res

@todoRouter.get('/get/{item}', response_model=ApiResponse)
async def get_todo(item: str):
    res = todoDb.model.getTodo(item=item)
    return res

@todoRouter.post('/create', response_model=ApiResponse)
async def createTodo(item: TodoCreate):
    res = await todoDb.model.createTodo(item.item)
    return res

@todoRouter.put('/update', response_model=ApiResponse)
async def updateTodo(item: TodoUpdate):
    res = await todoDb.model.updateTodo(item=item.item, action=item.action)
    return res

@todoRouter.delete('/delete', response_model=ApiResponse)
async def deleteTodo(item: str):
    res = await todoDb.model.deleteTodo(item)
    return res


