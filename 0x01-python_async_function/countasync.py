"""Module documentation"""
#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    """Coroutine to count"""
    print("One")
    await asyncio.sleep(1)
    print("two")


async def main():
    """Main coroutine"""
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
