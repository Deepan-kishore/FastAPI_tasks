import aiofiles
import os
import json


async def load_file(path) -> dict[str,str] :
    if os.path.exists(path):
        async with aiofiles.open(path,'r') as file:
            try:
                content = await file.read()
                todo = json.loads(content)
                return todo
            except Exception:
                print("Getting error in accessing file")
                should_create = input("Should I create one?")
                if should_create == "yes":
                    try:
                        async with aiofiles.open(path, "x") as file:
                            await file.write(json.dumps({},indent=2))
                            
                            return await load_file(path)
                    except Exception as e:
                        print("Error in creating file : ")
                        print(e)
                        print("Manualy starting todo")
                        todo = {}
                        return todo

    else:
            print("path doesnt exis => handle it")
    
    return {}


async def write_to_file(path,todo):
    async with aiofiles.open(path,'w') as file:
        try:
            await file.write(json.dumps(todo,indent=2))
        except Exception as e:
            print("Error in writing file : ")
            print(e)
        else:
            return "File saved"

def parsed_input(question, type):
    raw_answer = input(question)
    try:
        parsed_answer = type(raw_answer)
    except (ValueError,TypeError):
        print("Invalid entry. try again")
        return False
    else:
        return parsed_answer
