my_dict = {
    "b": 3,
    "a": 5,
    "d": 1,
    "c": 4
}

sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_by_value)
