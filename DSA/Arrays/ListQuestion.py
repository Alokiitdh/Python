list1 = ['a', 'b', 5, 6, 'c','d', 10, 'e']
list2 = []

prev_value = 0  # Initialize previous value

for item in list1:
    if isinstance(item, int):
        list2.append(item)  # Keep numbers unchanged
        prev_value = item  # Update prev_value
    else:
        list2.append(prev_value + 1)  # Replace with (previous value + 1)
        prev_value += 1  # Update prev_value

print(list2)
