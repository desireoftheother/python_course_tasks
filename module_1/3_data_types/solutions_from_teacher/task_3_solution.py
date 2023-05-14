NON_VALID_STRING: str = "Пароль не відповідає критеріям \
(не менше ніж 8 символів, наявність великих, маленьких літер, спецсимволів і цифр).\n\
Будь ласка, введіть пароль заново."

while True:
    password_1: str = input("Введіть пароль: ")
    password_2: str = input("Введіть пароль ще раз: ")
    if password_1 != password_2:
        print("Паролі не співпадають! Повторіть введення!")
        continue
    capital_count: int = 0
    small_count: int = 0
    numeric_count: int = 0
    special_symb_count: int = 0
    for letter in password_1:
        if letter.islower():
            small_count += 1
        elif letter.isupper():
            capital_count += 1
        elif letter.isnumeric():
            numeric_count += 1
        elif not (letter.isalpha() or letter.isnumeric()):
            special_symb_count += 1
    is_small_and_capital: bool = capital_count > 0 and small_count > 0
    is_numeric: bool = numeric_count > 0
    is_special_symbs: bool = special_symb_count > 0
    is_long_enough: bool = len(password_1) > 8

    if is_small_and_capital and is_numeric and is_special_symbs and is_long_enough:
        print("Пароль валідний! Дякую!")
        break
    else:
        print(NON_VALID_STRING)
