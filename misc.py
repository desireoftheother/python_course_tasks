from threading import Lock, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.first = Lock()
        self.second = Lock()
        self.third = Lock()
        self.fourth = Lock()

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        while self.i <= self.n:
            with self.first, self.second, self.third:
                if self.i % 3 == 0:
                    print("fizz")
                    self.i += 1

    # printBuzz() outputs "buzz"
    def buzz(self) -> None:
        while self.i <= self.n:
            with self.first, self.second:
                if self.i % 5 == 0:
                    print("buzz")
                    self.i += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self) -> None:
        while self.i <= self.n:
            with self.first:
                if self.i % 5 == 0 and self.i % 3 == 0:
                    print("fizzbuzz")
                    self.i += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self) -> None:
        while self.i <= self.n:
            if self.i % 5 != 0 and self.i % 3 != 0:
                print(self.i)
                self.i += 1

fb = FizzBuzz(15)
t1 = Thread(target=fb.fizz)
t2 = Thread(target=fb.buzz)
t3 = Thread(target=fb.fizzbuzz)
t4 = Thread(target=fb.number)

t2.start()
t3.start()

t1.start()

t4.start()