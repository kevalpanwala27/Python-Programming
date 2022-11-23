age = int(input("What is your age\n"))
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
result = f"You have {days_remaining} days, you have {weeks_remaining} weeks, you have {months_remaining} months"
print(result)

