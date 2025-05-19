my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Tashkent"
}

key = "age"

if key in my_dict:
    print(key, my_dict[key])
else:
    print("Key is not in Dictionary")