numbers = [3, 2, 8, 1, 6, 9, 2, 7, 2]

element = 2
indexs = []

for i in range(len(numbers)):
    if numbers[i] == element:
        indexs.append(i)

print(indexs)