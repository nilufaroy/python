my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Tashkent"
}

key = "age"

if key in my_dict:
    my_dict.update({key: 30 })
    print(my_dict)
else:
    print("Key is not in Dictionary")