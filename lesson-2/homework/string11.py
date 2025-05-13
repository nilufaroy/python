txt = input("Enter the sentence: ")

check = any(char.isdigit() for char in txt)

print(check)
