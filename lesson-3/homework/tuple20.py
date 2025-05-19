original_tuple = (1, 2, 3, 4, 5, 6)
nested_list = []

for i in range(0,len(original_tuple),2):
    nested_list.append(tuple(original_tuple[i:i+2]))
    nested_tuple = tuple(nested_list)

print(nested_tuple)