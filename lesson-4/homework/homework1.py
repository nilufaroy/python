list1 = list(map(int, input("Enter numbers for list1 separated by spaces: ").split()))
list2 = list(map(int, input("Enter numbers for list2 separated by spaces: ").split()))

uncommon = []
for i in list1:
    if i not in list2:
        uncommon.append(i)
    
for j in list2:
    if j not in list1:
        uncommon.append(j)
    
print(uncommon)
