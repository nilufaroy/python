my_tuple = (7, 13, 7, 21, 42, 13, 7)

unique_tuple = set(my_tuple)

first_largest = max(unique_tuple)
unique_tuple.remove(first_largest)

second_largest = max(unique_tuple)

print(second_largest)
