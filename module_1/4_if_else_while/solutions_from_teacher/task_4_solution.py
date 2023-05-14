GREETING_TEXT: str = """Привіт і вітаю в імпровізованому калькуляторі! 
Введи calculate для того щоб зробити просту арифметичну операцію і end щоб завершити програму!"""

CALCULATE_TEXT: str = """Обрано команду calculate!
Ти можеш скористатися однією з чотирьох арифметичних операцій: +, -, /, *.
Програма приймає на вхід виключно цілі числа."""

print(GREETING_TEXT)

while True:
    command: str = input("Введи команду: ")
    if command == "calculate":
        print(CALCULATE_TEXT)
        while True:
            first_operand_str: str = input("Введи перший операнд: ")
            if not first_operand_str.isnumeric():
                print("Перший операнд не валідний! Введи валідне ціле число!")
                continue
            second_operand_str: str = input("Введи другий операнд: ")
            if not second_operand_str.isnumeric():
                print("Другий операнд не валідний! Введи валідне ціле число!")
                continue
            operator_str: str = input("Введи оператор: ")
            if operator_str not in "+-/*" or len(operator_str) > 1:
                print("Оператор не валідний! Введи один з дозволених операторів (+, -, /, *)")
                continue
            break
        first_operand: int = int(first_operand_str)
        second_operand: int = int(second_operand_str)
        if operator_str == "+":
            result = first_operand + second_operand
        elif operator_str == "-":
            result = first_operand - second_operand
        elif operator_str == "*":
            result = first_operand * second_operand
        elif operator_str == "/":
            result = first_operand / second_operand
        print(f"Результат виконування операції: {result}")
        print("Дякую за довіру! Переводжу в меню вибору команди.")
    elif command == "end":
        print("Отримано команду end, завершую роботу!")
        break
    else:
        print("Отримано помилкову команду! Введи валідну команду (calculate або end)!")
