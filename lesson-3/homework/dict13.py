my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

inverted_dict = {value: key for key, value in my_dict.items()}

print(inverted_dict)
