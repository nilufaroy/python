numbers = [12, -7, 0, 34, -25, 0, 18, -43, 29, -1, 5, 12, 34, 0, 34]

unique_numbers = []

for number in numbers :
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
