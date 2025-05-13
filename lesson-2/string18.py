txt = input("Enter a string: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")

start = txt.startswith(start_word)
end = txt.endswith(end_word)

print(f"Starts with: {start}")
print(f"Ends with: {end}")
