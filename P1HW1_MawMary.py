# Mary Maw
# June 25, 2025
# P1HW1
# Code that collects information, processes and displays user results

print("---Calculating Exponents---")
base_value = int(input("\nEnter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent
print("\n", base_value, "raised to the power of", exponent, "is", result, "!!")

print("\n---Addition and SUbtraction")

starting_integer = int(input("\nEnter a starting integer: "))
add_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))
product = starting_integer + add_integer - subtract_integer

print("\n", starting_integer, "+", add_integer, "-", subtract_integer, "is equal to", product)
