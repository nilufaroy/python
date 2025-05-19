numbers = [1,2,4,52,5,6,7,89,12,2,2]

odd = []

for number in numbers:
    if number%2 != 0:
        odd.append(number)

print(odd)  