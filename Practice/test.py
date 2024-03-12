'''For drawing graphics in Python, you can use the turtle module. The turtle module provides a simple drawing library that is great for beginners and allows you to draw various shapes, including straight lines, using a pen-like interface.
import turtle'''

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
pen = turtle.Turtle()

# Move the pen to the starting position
pen.penup()
pen.goto(-100, 0)  # Adjust the coordinates as needed

# Lower the pen to start drawing
pen.pendown()

# Draw a straight line
pen.forward(200)  # Adjust the length as needed

# Close the turtle graphics window when clicked
screen.exitonclick()
