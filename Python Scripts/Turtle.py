# TURTLE library

import turtle 	# import turtle library

# Draw a square
t = turtle.Turtle()		# initialize a turtle
t.forward(100)		# move forward for 100 pts
t.right(90)			# move forward for 100 pts
t.forward(100)		# move forward for 100 pts
t.right(90)			# move forward for 100 pts
t.forward(100)		# move forward for 100 pts
t.right(90)			# move forward for 100 pts
t.forward(100)		# move forward for 100 pts
t.right(90)			# move forward for 100 pts

t.clear()           # clears turtle's path


# Change colors
t.screen.bgcolor('black') # change background color to black
t.screen.bgcolor('brown') # change background color to brown

t.color("blue") # change turtle color to blue


# Draw a slanted rectangle
t.left(30)
t.fd(100)
t.left(90)
t.fd(200)
t.left(90)
t.fd(100)
t.left(90)
t.fd(200)

t.clear()         

# Draw a star using a loop
for i in range(0, 5):
	t.forward(100)		# move forward for 100 pts
	t.right(144)		   # right turn for 144 degrees
    
t.clear()        

# Draw a circle
t.circle(50,360)        # size of circle radius, rotation degrees
t.clear()  

# Change shape of turtle
# available shapes are: arrow, circle, square, triangle turtle, classic
t.shape("turtle")       # change shape to turtle
t.shapesize(20)         # change size
t.shapesize(1) 



# Filling in shapes
t.screen.bgcolor("black")
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.hideturtle()          # hides the turtle


# For more on TURTLE:
# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
# http://www.instructables.com/id/Easy-Designs-Turtle-Graphics-Python/




