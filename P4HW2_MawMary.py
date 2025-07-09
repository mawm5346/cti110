# Mary Maw
# July 8, 2025
# P4HW1
#
# Pseudocode:
# Ask user how many scores they want to enter
# Create an empty list
# Get each score: 
# - If score is invalid, ask again
# - If score is valid, add to list
# Drop the lowest score
# Find the average
# Find the letter grade
# Display results

# Ask user how many scores
num_scores = int(input("How many scores do you want to enter? "))

# Empty list to hold scores
student_scores = []

# Loop to collect valid scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                student_scores.append(score)
                break  
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid. Enter a numeric score.")

# Find and remove lowest score
lowest_score = min(student_scores)
student_scores.remove(lowest_score)

# Calculate average of modified list
average = sum(student_scores) / len(student_scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------ Results ------")
print(f"Lowest Score    : {lowest_score}")
print(f"Modified List   : {student_scores}")
print(f"Scores Average  : {average:.2f}")
print(f"Grade           : {grade}")
  
        