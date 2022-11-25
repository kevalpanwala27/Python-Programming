print("Welcome to roller coaster")
height = int(input("What is your height in cm ?\n"))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is you age ?\n"))
    if age < 12:
        print("Please pay me $5 ")
    elif age <= 18:
        print("Please pay me $7 ")
    else:
        print("Please pay me $12 ")
else:
    print("Sorry, you have to grow taller")
