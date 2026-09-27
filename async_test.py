import asyncio

async def hello():
    print("Hello from Asyncio!")
    await asyncio.sleep(1)
    print("Asyncio is working!")

asyncio.run(hello())