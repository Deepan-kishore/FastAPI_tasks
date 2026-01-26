import json
import os

import aiofiles


async def load_file(path):
    if os.path.exists(path):
        try:
            async with aiofiles.open(path, "r") as file:
                raw_file = await file.read()
                todo = json.loads(raw_file)
        except:
            return "Error in reading files"
        else:
            return todo
    else:
        print("File does not exist, creating one")
        try:
            async with aiofiles.open(path, "w") as file:
                todo = {}
                await file.write(json.dumps(todo))
        except:
            return "Error in reading files"
        else:
            return await load_file(path)


async def write_to_file(path, todo):
    if os.path.exists(path):
        try:
            async with aiofiles.open(path, "w") as file:
                await file.write(json.dumps(todo))
        except:
            return "Error while updating file"
        else:
            return "File Updated"
        
    else: return "File not found"
