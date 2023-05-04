import asyncio
import itertools
#import math
#import time


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end='')


async def slow() -> int:
    await asyncio.sleep(3)
    #time.sleep(3)
    return 42


def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("thinking!"))
    print(f"spinner object: {spinner}")
    #result = is_prime(5_000_111_000_222_021)
    #result = await is_prime(5_000_111_000_222_021)
    result = await slow()
    #await asyncio.sleep(2)
    spinner.cancel()
    return result


# def is_prime(n: int) -> bool:
#    """This is an example how concurrency deals with the CPU intensive function"""
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if not n % 2:
#         return False
#     root = math.isqrt(n)
#     for i in range(3, root + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# async def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if not n % 2:
#         return False
#     root = math.isqrt(n)
#     for i in range(3, root + 1, 2):
#         if n % i == 0:
#             return False
#         if i % 100_000 == 1:
#             await asyncio.sleep(0)
#     return True


if __name__ == "__main__":
    main()
