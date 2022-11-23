num_char = len(input("What is your name\n"))
print(type(num_char))  # This is used to check the form of data types
new_num_char = str(num_char)  # Doing type casting i.e. type conversion.
print("Your name has " + new_num_char + " characters")  # This will show error.
