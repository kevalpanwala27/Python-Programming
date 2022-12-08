import random

print("welcome to the bank roulette exercise")
names_string = input("Give me everybody's name, separated by commas\n")
names = names_string.split(", ")

random_names = random.choice(names)
print(random_names)

