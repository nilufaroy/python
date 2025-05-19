my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Tashkent"
}

key = "age"

if key in my_dict:
    del my_dict[key]
    print(f"Key '{key}' removed.")
else:
    print("Key is not in the dictionary")

print(my_dict)
