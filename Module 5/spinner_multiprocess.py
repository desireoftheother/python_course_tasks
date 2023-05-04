import itertools
import time
import math
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end='')


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    #result = is_prime(5_000_111_000_222_021)
    done.set()
    spinner.join()
    return result


def main():
    result = supervisor()
    print(f"Answer: {result}")


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

if __name__ == "__main__":
    main()
