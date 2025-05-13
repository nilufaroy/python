text = input("Enter a string: ").lower()
vowels = "aeiou"
v = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
letters = len(text) 

c = letters - v
print("Vowels:", v)
print("Consonants:", c)
