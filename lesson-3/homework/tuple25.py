my_tuple = (5, 12, 7, 8, 25, 3, 18, 3, 7, 5)

my_list = list(my_tuple)
unique_list = []

for number in my_tuple:
    if number not in unique_list:
        unique_list.append(number)

unique_tuple = tuple(unique_list)
print(unique_tuple)        