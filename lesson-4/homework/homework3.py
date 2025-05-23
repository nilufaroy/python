txt = input("Matn kiriting: ")
vowels = 'aeiou'
result = []
i = 0
count = 0

while i < len(txt):
    result.append(txt[i])
    count += 1

    if count == 3:
        if i == len(txt) - 1:
            break
        elif txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
            if i + 1 < len(txt) - 1:
                result.append(txt[i + 1])
                result.append('_')
                i += 1
        else:
            result.append('_')
        count = 0
    i += 1

print(''.join(result))

