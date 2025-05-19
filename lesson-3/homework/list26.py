numbers = [1,2,4,52,5,6,7,89,12,2,2]

length = len(numbers)

if length%2 != 0:
    mid = length//2
    print(numbers[mid])
else:
    mid1 = (length - 1)//2
    mid2 = mid1 + 1
    print(mid1)
    print(numbers[mid1], numbers[mid2])

