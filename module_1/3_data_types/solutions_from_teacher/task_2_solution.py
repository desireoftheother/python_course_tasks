command = input("Привіт! Введи команду fac для підрахунку факторіалу і fib для підрахунку числа Фібоначчі! ")

if command == "fac":
    n = int(input("Вибрано підрахунок факторіалу! Введіть число, для котрого треба підрахувати факторіал: "))
    if n == 1 or n == 0:
        fac_while = 1
    else:
        i = 1
        fac_while = 1
        while i < n:
            i += 1
            fac_while *= i
    print(f"Факторіал числа {n} дорівнює {fac_while}, імплементація через while")
    fac_for = 1
    for j in range(0, n+1):
        if j == 0:
            fac_for = 1
        else:
            fac_for *= j
    print(f"Факторіал числа {n} дорівнює {fac_for}, імплементація через for")
if command == "fib":
    n = int(input("Вибрано підрахунок числа Фібоначчі! Введіть порядок числа Фібоначчі: "))
    f_1_while = 0
    f_2_while = 1
    if n == 0:
        fib_while = f_1_while
    if n == 1:
        fib_while = f_2_while
    else:
        i = 1
        fib_while = 0
        while i < n:
            fib_while = f_1_while + f_2_while
            f_1_while = f_2_while
            f_2_while = fib_while
            i += 1
    print(f"Число Фібоначчі порядку {n} дорівнює {fib_while}, імплементація через while")
    f_1_for = 0
    f_2_for = 1
    fib_for = 0
    for i in range(1, n+1):
        fib_for = f_1_for + f_2_for
        f_1_for = f_2_for
        f_2_for = fib_for
    print(f"Число Фібоначчі порядку {n} дорівнює {fib_while}, імплементація через for")
