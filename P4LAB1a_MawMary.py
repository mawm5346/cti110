#Mary Maw
#July 7, 2025
#P4LAB1
#Use turtle and loops to draw a square and a triangle

#Import the library
import turtle


#Create the turtle window and drawing object
win = turtle.Screen()
t = turtle.Turtle()


#Set turtle options
t.pensize(5)
t.pencolor("pink")
t.shape("arrow")

#Code to draw the shapes
for side in range(4):
    t.forward(100)
    t.left(90)

#While loop that executes 3 times
sides = 3

while sides > 0:
    t.forward(100)
    t.left(120)
    sides = sides - 1

#Wait for user to close Window
win.mainloop()
