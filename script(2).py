# User for input
name = input("What is your name? ")
age = input("How old are you? ")

# Change the user's age to an integer
age = int(age)

# Performing some calculations
year_born = 2023 - age
hundredth_birthday_year = year_born + 100

# Results
print("Hello, " + name + "!")
print("You were born in " + str(year_born))
print("You will turn 100 in the year " + str(hundredth_birthday_year))
