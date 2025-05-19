my_tuple = (5, 12, 8, 25, 3, 18, 7)

reversed_list = list(my_tuple)
reversed_list.reverse()
reversed_tuple = tuple(reversed_list)

is_paliandrome = my_tuple == reversed_tuple

if is_paliandrome is True:
    print("Tuple is paliandrome")
else:
    print("Tuple is not paliandrome")