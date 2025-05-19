my_set = {12, 57, 89, 3, 44, 76}
odd = set()

for num in my_set:
    if num%2 != 0:
        odd.add(num)

print(odd)
