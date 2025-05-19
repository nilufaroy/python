my_dict = {
    "a": 1,
    "b": {"x": 10, "y": 20},
    "c": 3
}

has_nested_dict = any(isinstance(value, dict) for value in my_dict.values())

print("Contains nested dictionary:", has_nested_dict)
