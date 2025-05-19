my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

target = 10

keys_with_value = [key for key, value in  my_dict.items() if target == value]
print(keys_with_value)