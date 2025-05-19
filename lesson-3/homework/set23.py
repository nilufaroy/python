import random

length = 8          
lower_bound = 10      
upper_bound = 50          

random_set = set(random.sample(range(lower_bound, upper_bound + 1), length))

print("Random Set:", random_set)
