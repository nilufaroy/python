###names = ['Nilufar', 'Laziz', 'Nozigul', 'Nilufar', 'Malika', 'Jamshid', 'Jamoliddin', 'Nozigul']

###unique_names = list(set(names))

###print(unique_names)

names = ['Nilufar', 'Laziz', 'Nozigul', 'Nilufar', 'Malika', 'Jamshid', 'Jamoliddin', 'Nozigul']
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)       
