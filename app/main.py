import asyncio
from app.models import AsyncTodo


async def display_menu() -> None:
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("Welcome to TODO App")
    print("=" * 50)
    print("1. Add Todo")
    print("2. Delete Todo")
    print("3. Update Todo")
    print("4. Show All Todos")
    print("5. Get Specific Todo")
    print("6. Refresh Menu")
    print("7. Exit")
    print("=" * 50)


async def handle_add(todo: AsyncTodo) -> None:
    """Handle adding a new todo"""
    item = input("Enter todo item name: ").strip()
    if not item:
        print("❌ Item name cannot be empty!")
        return
    
    result = await todo.add(item)
    print(f"✅ {result}")


async def handle_delete(todo: AsyncTodo) -> None:
    """Handle deleting a todo"""
    item = input("Enter todo item name to delete: ").strip()
    if not item:
        print("❌ Item name cannot be empty!")
        return
    
    result = await todo.delete(item)
    print(f"✅ {result}")


async def handle_update(todo: AsyncTodo) -> None:
    """Handle updating a todo"""
    item = input("Enter todo item name to update: ").strip()
    if not item:
        print("❌ Item name cannot be empty!")
        return
    
    action = input("What do you want to change it to? (not Completed/Started/completed): ").strip()
    if not action:
        print("❌ Action cannot be empty!")
        return
    
    result = await todo.update(item, action)
    print(f"✅ {result}")


async def handle_show_all(todo: AsyncTodo) -> None:
    """Handle showing all todos"""
    result = todo.get(getAll=True)
    
    if isinstance(result, str):
        print(f"📝 {result}")
        return
    
    print("📝 Your Todos:")
    print("-" * 50)
    if not result:
        print("No todos found!")
    else:
        for i, item in enumerate(result, 1):
            status = todo.todo.get(item, "Unknown")
            print(f"{i}. {item:<30} [{status}]")
    print("-" * 50)


async def handle_get_one(todo: AsyncTodo) -> None:
    """Handle getting a specific todo"""
    item = input("Enter todo item name: ").strip()
    if not item:
        print("❌ Item name cannot be empty!")
        return
    
    result = todo.get(item)
    print(f"📝 {item}: {result}")


async def main() -> None:
    """Main async function to run the todo app"""
    try:
        # Create and load todo instance
        print("🔄 Loading your todos...")
        todo = await AsyncTodo.create()
        print("✅ Todos loaded successfully!\n")
        
        # Main loop
        while True:
            await display_menu()
            
            option = input("Enter your option (1-7): ").strip()
            
            try:
                option_num = int(option)
            except ValueError:
                print("❌ Invalid option! Please enter a number between 1-7")
                continue
            
            if option_num == 1:
                await handle_add(todo)
            
            elif option_num == 2:
                await handle_delete(todo)
            
            elif option_num == 3:
                await handle_update(todo)
            
            elif option_num == 4:
                await handle_show_all(todo)
            
            elif option_num == 5:
                await handle_get_one(todo)
            
            elif option_num == 6:
                print("🔄 Refreshing menu...")
                continue
            
            elif option_num == 7:
                print("👋 Thank you for using TODO App! Goodbye!")
                break
            
            else:
                print("❌ Invalid option! Please enter a number between 1-7")
    
    except KeyboardInterrupt:
        print("\n\n👋 App interrupted by user. Goodbye!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
