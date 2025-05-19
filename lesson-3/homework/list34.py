numbers = [3, 2, 8, 1, 6, 9, 2, 7, 2]

rotated_list = []

rotated_list.append(numbers[-1])
numbers.pop()
for number in numbers:
    rotated_list.append(number)

print(rotated_list)