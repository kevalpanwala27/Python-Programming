print("Welcome to roller coaster")
height = int(input("What is your height in cm ?\n"))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is you age ?\n"))
    if age < 12:
        bill = 5
        print("Child tickets pay me $5 ")
    elif age <= 18:
        bill = 7
        print("Youths tickets pay me $7 ")
    else:
        bill = 12
        print("Adults tickets pay me $12 ")

    wants_photo = input("Do you want a photo taken ? Y or N. ")
    if wants_photo == 'Y':
        bill += 3

    print(f"Your total bill is {bill}")

else:
    print("Sorry, you have to grow taller")

