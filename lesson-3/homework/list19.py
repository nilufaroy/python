list_elem = [1,2,4,52,5,6,7,89,12,2,2]

replace_elem = int(input("enter the element to replace:"))
new_elem = int(input("Enter the new element:"))

if replace_elem in list_elem:
    index = list_elem.index(replace_elem)
    list_elem[index] = new_elem

print(list_elem)