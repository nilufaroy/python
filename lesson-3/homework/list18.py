main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]

found = False
for i in range(len(main_list)-len(sub_list)+1):
    if main_list[i:i+len(sub_list)]:
        found = True

print(found)