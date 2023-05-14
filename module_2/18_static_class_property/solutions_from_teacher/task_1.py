def generate_sublists(lst):
    n = len(lst)
    for i in range(n + 1):
        for j in range(i):
            yield lst[j:i]

lst = [1, 2, 3, 4, 5]
for sublst in generate_sublists(lst):
    print(sublst)
