from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.router.router import todoRouter
from app.db.todoDb import initialteTodo
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("application starting setup from asynccontextmanager")
    await initialteTodo()
    yield
    print("application closing steps from asynccontextmanager")

# Create FastAPI instance
app = FastAPI(
    title="Todo API",
    description="A simple Todo API using FastAPI",
    version="1.0.0",
    lifespan=lifespan
)



# Include the todo router

app.include_router(todoRouter, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    """Root endpoint - API documentation and information"""
    return JSONResponse({
        "message": "Welcome to Todo API",
        "version": "1.0.0",
        "description": "A simple Todo API using FastAPI",
        "documentation": {
            "interactive_docs": "/docs",
            "alternative_docs": "/redoc",
            "openapi_schema": "/openapi.json"
        },
        "available_endpoints": {
            "todos": {
                "GET /api/todos/get": "Get all todos",
                "GET /api/todos/get/{item}": "Get a specific todo by name",
                "POST /api/todos/create": "Create a new todo (requires: {\"item\": \"todo name\"})",
                "PUT /api/todos/update": "Update a todo status (requires: {\"item\": \"todo name\", \"action\": \"completed/incompleted\"})",
                "DELETE /api/todos/delete": "Delete a todo (requires query param: ?item=todo_name)"
            },
            "health": {
                "GET /health": "Health check endpoint"
            }
        },
        "quick_start": "Visit /docs to try the API with interactive Swagger UI"
    })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}