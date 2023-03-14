import copy

example_list = ["a", "b", ["c"], [[["d"]]], ["e", ["f", "g"]]]

start_list = copy.deepcopy(example_list)

is_list_nested = True
final_list = []
while is_list_nested:
    nested_list = []
    nested_count = 0
    for item in start_list:
        if not isinstance(item, list):
            final_list.append(item)
        else:
            nested_list += item
            nested_count += 1
    if nested_count > 0:
        start_list = nested_list
    else:
        is_list_nested = False

print(final_list)
