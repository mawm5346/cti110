# Mary Maw
# July 3, 2025
# P2HW1
# Program does basic math on numbers entered, formatted nicely

print("This program calculates and displays travel expenses ")

# Ask user to enter their budget
budget = float(input("\nWhat is your budget? "))

# Ask user to enter travel destination 
location = input("\nWhere is your travel destination? ")

# Ask user for amount they will spend on gas
gas = float(input("\nHow much will you spend on gas? "))

# Ask user for amount they will spend on accomdation 
accomadation = float(input("\nHow much will you spend on accomadation? "))

# Ask user for amount they will spend on food
food = float(input("\nHow much will you spend on food? "))

# Add expenses
expenses = gas + accomadation + food

# Subtract expenses from budget
result = budget - expenses

# Display results
print("\n" + "Travel Expenses".center(40, "-"))
print(f"{'Location:':<20}{location}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accomadation:':<20}${accomadation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("-" * 40)
print(f"{'Remaining Balance:':<20}${result:.2f}")

