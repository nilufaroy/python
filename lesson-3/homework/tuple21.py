my_tuple = (1, 2, 3, 4, 5, 6)
num = 3

repeated = []

for elem in my_tuple:
    for i in range(num):
        repeated.append(elem)

repeated_tuple = tuple(repeated)
print(repeated_tuple)
