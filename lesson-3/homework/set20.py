set1 = {12, 3, 45, 28, 7, 19, 33}
set2 = {5, 39, 42, 48, 33, 7}

same = set1.symmetric_difference(set2)

if same == 0:
    print("No common elements")
else:
    print("Has common elements")

