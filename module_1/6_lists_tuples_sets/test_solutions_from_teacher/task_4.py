list_for_sorting = [2, 5, 7, 2, 8, 10, 1, -1, -2]

# Це реалізація так званого bubble sort. Дуже неоптимальний алгоритм, насправді

for index1 in range(0, len(list_for_sorting)):
    element_1 = list_for_sorting[index1]
    for index2 in range(0, len(list_for_sorting)):
        element_2 = list_for_sorting[index2]
        if element_1 < element_2:
            list_for_sorting[index1], list_for_sorting[index2] = list_for_sorting[index2], list_for_sorting[index1]

print(list_for_sorting)
