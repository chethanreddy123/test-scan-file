import asyncio
import string

data = {
    "John": "English",
    "Steve": "Mathematics",
    "Sarah": "Science"
}

async def get_subject(name: str) -> str:
    await asyncio.sleep(2)  
    subject = data[name]
    return subject

async def main():
    name = "John"
    subject = await get_subject(name)
    print(f"{name} teaches {subject} in school")

asyncio.run(main())


