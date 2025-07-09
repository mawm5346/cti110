#Mary Maw
#July 7, 2025
#P4HW1
#Multiplication table

n = 0
run_program = "yes"

while run_program == "yes": 
    n = int(input("Enter an integer: "))

    if n >= 0:
        for i in range (1, 13):
            print (f"{n} x {i} = {n * i}")
    else:
        print("This program does not handle negative numbers")

    run_program = input("\nWould you like to run the program again? ")

print("Exiting program... ")

    
    
    
    
