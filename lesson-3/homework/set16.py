my_set = {12, 57, 89, 3, 44, 76}
even = set()

for num in my_set:
    if num%2 == 0:
        even.add(num)

print(even)
