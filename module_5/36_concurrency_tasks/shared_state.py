from typing import Self, Any, Iterable
from dataclasses import dataclass
from threading import Thread, get_ident
from time import sleep


@dataclass
class Node:
    value: Any
    next: Self | None = None

    def __repr__(self) -> str:
        return f"Node with value {self.value}"


class LinkedListWithIterator:
    def __init__(self, root) -> None:
        self.root: Node = root
        self.current: Node = root

    def __iter__(self):
        return self

    def __next__(self):
        if self.current.next:
            next: Node = self.current.next
            self.current = next
            return next
        else:
            raise StopIteration

    @classmethod
    def create_from_iterable(cls, iterable: Iterable) -> Self:
        prev_node: Node = Node(value=iterable[0])
        root: Node = prev_node
        for index, item in enumerate(iterable, start=1):
            node: Node = Node(value=item)
            prev_node.next = node
            prev_node = node
        result = cls(root=root)
        return result


def print_within_thread(iterable: Iterable, times: int):
    for index, item in enumerate(iterable):
        if index == times:
            break
        sleep(1)
        print(f"Object {item} within thread {get_ident()}")


ll: LinkedListWithIterator = LinkedListWithIterator.create_from_iterable(range(10))

# for i in ll:
#     print(i)

t1 = Thread(target=print_within_thread, args=(ll, 10))
t2 = Thread(target=print_within_thread, args=(ll, 10))

t1.start()
t2.start()

print_within_thread(ll, 10)
