# Example is taken from Fluent Python book

import itertools
import time
from multiprocessing import Process, Event


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = char + " " + msg
        print(status, flush=True, end="\r")
        if done.wait(0.09):
            break
    print(" " * len(status), end="\r")


def slow_function() -> int:
    time.sleep(7)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))
    print("spinner object:", spinner)
    spinner.start()
    result = slow_function()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    main()
