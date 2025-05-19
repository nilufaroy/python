my_tuple = (7, 13, 7, 21, 42, 13, 7)

unique_tuple = set(my_tuple)

first_min = min(unique_tuple)
unique_tuple.remove(first_min)

second_min = min(unique_tuple)

print(second_min)
