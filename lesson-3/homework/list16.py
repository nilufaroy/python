numbers = [2,4,67, 88, 23, 98, 261, 356, 238832, 89, 3634, 9876]

odd = []
count = 0

for number in numbers:
    if number%2 != 0:
        odd.append(number)
        count +=1

print(count)        