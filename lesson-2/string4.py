txt = input("Enter a string: ")

if txt == txt[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
