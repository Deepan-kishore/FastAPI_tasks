from fastapi import FastAPI
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
    """Root endpoint"""
    return {"message": "Welcome to Todo API"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}