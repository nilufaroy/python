my_tuple = (5, 12, 3, 8, 25, 3, 18, 7)
elem = 3

my_list = list(my_tuple)

my_list.remove(elem)

new_tuple = tuple(my_list)
print(new_tuple)