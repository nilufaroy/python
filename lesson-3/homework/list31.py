numbers = [3, 8, 1, 6, 9, 2, 7]
new_list = []

number = 4

for number in numbers:
    new_list.extend([number]*4)

print(new_list)    
