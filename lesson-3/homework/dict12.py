my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

value_to_count = 10

count = list(my_dict.values()).count(value_to_count)

print(f"The value {value_to_count} appears {count} times.")
