from Marker import marker
import asyncio


async def exit():
    await exit_ = input()

    return exit_

async def main():
    task = asyncio.create_task(exit())

    await task

asyncio.run(main())

flag = True
while flag:
    marker()
    com_exit = exit()
    if com_exit == "/":
        break