# Mary Maw
# July 3, 2025
# P2HW2
# Program asks user to enter grades for six modules
# calculates lowest, highest, sum and average

# Pseudocode:
# Ask the user to enter 6 grades 
# Store the grades in a list
# Find the lowest, highest, total, and average grade
# Display the results with proper formatting


# Ask user to enter grades for Module 1-6
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# List of grades
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate lowest, highest, sum and average grades
min_Grade = min(grades)
max_Grade = max(grades)
sum_Grade = sum(grades)
ave_Grade = sum(grades) / 6


# Display results
print("\n" + "Results".center(40, "-"))
print(f"{'Lowest Grade:':<20}{min_Grade:.1f}")
print(f"{'Highest Grade:':<20}{max_Grade:.1f}")
print(f"{'Sum of Grades:':<20}{sum_Grade:.1f}")
print(f"{'Average:':<20}{ave_Grade:.1f}")
print("-" * 40)