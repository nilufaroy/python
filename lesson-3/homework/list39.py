numbers = [12, -7, 34, -25, 0, 18, -43, 29, -1, 5]

sublist_size = 3
nested_list = []

i = 0
while i<len(numbers):
    nested_list.append(numbers[i:i+sublist_size])
    i += sublist_size

print(nested_list)