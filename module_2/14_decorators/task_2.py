# Задача 2. Імплементувати lru_cache
#
# lru_cache - декоратор, що запам'ятовує останні виклики функції й якщо вона ще раз викликається з цими аргументами, то він дістає її значення з кешу замість виконання.
#
# Імплементуйте декоратор, котрий дозволяє зберігати останні виклики функції в якомусь словнику і звертатися до них за потреби.
#
# Для простоти вважаємо, що ми маємо справу з функціями однієї змінної

from functools import wraps

def my_cache(func):
    container = dict()
    def wraps(*args, **kwargs):
        call = (func.__name__, args, kwargs)
        if call in container.keys():
            a = container[call]
            return a
        else:
            a = func(*args, **kwargs)
            container[call] = a
            return a
    return wraps

@my_cache
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@my_cache
def factorial(n):
    pass

print(fib.__name__)
