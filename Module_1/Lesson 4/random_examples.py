import random

print(f"Випадкове число від 0 до 1: {random.random()}")

print(f"Випадкове ціле число від 0 до 19: {random.randint(0, 19)}")

random.seed(1995)
print(f"Залежність результату генерації псевдовипадкових чисел від величини seed. "
      f"Наступне число, навідміну від попередніх, не буде змінюватися поки ми не змінимо seed: {random.random()}")
