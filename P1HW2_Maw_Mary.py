# Mary Maw
# June 26, 2025
# P1HW2
# Program does basic math on numbers entered

print("This program calculates and displays travel expenses ")

# Ask user to enter their budget
budget = float(input("\nWhat is your budget? "))

# Ask user to enter travel destination 
destination = input("\nWhere is your travel destination? ")

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
print("\n--- Travel Expenses ---")
print("Location: ", destination)
print("Initial Budget: $", budget)
print("\nFuel: $", gas)
print("Accomadation: $", accomadation)
print("Food: $", food)
print("\nRemaining Balance:", result)