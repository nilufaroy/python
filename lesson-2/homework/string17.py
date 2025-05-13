txt = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join('*' if char in vowels else char for char in txt)
print(result)
