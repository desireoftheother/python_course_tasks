# Задача 1. Калькулятор

# Написати консольний калькулятор, котрий приймає на вхід рядок виду 2+1 і виконує відповідну операцію над числами.
#
# Программа має працювати для всіх чисел. Якщо число невалідне, програма має повторювати запит на введення числа
#
# Бажано для вирішення цієї задачі використати регулярні вирази

# Регулярний вираз для знаходження знаків операцій над числами: (\+|\*\-|\\|\\\\|\%)

# Регулярний вираз для перевірки числа на те, чи є воно int: ^[0-9]+$

# Регулярний вираз для перевірки числа на те, чи є воно float: ^[0-9]+\.[0-9]+$