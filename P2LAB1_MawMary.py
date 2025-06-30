# Mary Maw
# June 30, 2025
# P2LAB1
# Using math expressions
import math

# Get radius user

radius = float(input("What is the radius of the circle? "))

# Calculate circum, diameter, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

# Display results
print(f"\nThe diameter of the circle is {diam:.1f}")
print(f"\nThe circumference of the circle is {cir:.2f}")
print(f"\nThe area of the circle is {area:.3f}")



