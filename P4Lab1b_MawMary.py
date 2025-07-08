#Mary Maw
#July 7, 2025
#P4Lab1b
#Using turtle graphics to write first and last initials

#Turtle options
import turtle

win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.pencolor("green")
t.shape("arrow")

# Write first initial "M"
t.left(90)
t.forward(100)
t.right(135)
t.forward(70)
t.left(90)
t.forward(70)
t.right(135)
t.forward(100)

# Write spacing
t.penup()
t.right(90)     # face right
t.forward(100)  # move right
t.left(90)      # face up again
t.pendown()

# Second "M"
t.forward(100)
t.right(135)
t.forward(70)
t.left(90)
t.forward(70)
t.right(135)
t.forward(100)

win.mainloop()


