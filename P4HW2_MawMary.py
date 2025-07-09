# Mary Maw
# July 8, 2025
# P4HW2
# Program calculates gross pay for multiple employees, determined by user
# Calculates total amount paid for overtime, total amount paid for regular
# pay, and total amount paid for all employees

# Initialize totals
total_employees = 0
total_regular_pay = 0.0
total_overtime_pay = 0.0
total_gross_pay = 0.0

# Loop
while True:
    employee = input("Enter employee's name or 'Done' to terminate: ")

    if employee.lower() == "done":
        break

    try:
        hours_worked = float(input(f"How many hours did {employee} work? "))
        pay_rate = float(input(f"What is {employee}'s pay rate? "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours and pay rate.")
        continue

    # Calculate regular and overtime pay
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    # Display employee pay details
    print("\n----------------------------")
    print(f"Employee Name: {employee}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<17}{'Regular Pay':<17}{'Gross Pay':<12}")
    print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<17.2f}{regular_pay:<17.2f}{gross_pay:<12.2f}")
    print("------------------------------\n")

# Final summary
print("\n========== Payroll Summary ==========")
print(f"Total Employees Entered : {total_employees}")
print(f"Total Overtime Pay      : ${total_overtime_pay:.2f}")
print(f"Total Regular Pay       : ${total_regular_pay:.2f}")
print(f"Total Gross Pay         : ${total_gross_pay:.2f}")
print("=====================================\n")
