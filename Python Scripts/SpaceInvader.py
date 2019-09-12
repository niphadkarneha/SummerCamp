import turtle
import math
import random
import winsound

def moveleft():
    x = player.xcor()
    x = x - playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def moveright():
    x = player.xcor()
    x = x + playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def fire():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x, y)
        bullet.showturtle()
        winsound.PlaySound("SystemExit", winsound.SND_ASYNC)

def isCollision(t1, t2):
    d = math.sqrt((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)
    if d < 15:
        return True
    else:
        return False

# setup the screen
wn = turtle.Screen()
wn.bgcolor("black")

# register the shapes
turtle.register_shape("C:/Users/Andrew/Desktop/invader.gif")
turtle.register_shape("C:/Users/Andrew/Desktop/player.gif")

# draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.color("blue")
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("C:/Users/Andrew/Desktop/player.gif") # replace with location of player gif file
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 10

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("C:/Users/Andrew/Desktop/invader.gif") # replace with location of invader gif file
enemy.penup()
enemy.speed(0)
enemy.setposition(random.randint(-280, 280), 250)
enemyspeed = 1

# create the playerbullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 10
bulletstate = "ready"

turtle.listen()
turtle.onkey(moveleft, "Left")
turtle.onkey(moveright, "Right")
turtle.onkey(fire, "space")
turtle.tracer(0, 0)

while True:
    # move the enemy
    x = enemy.xcor()
    x = x + enemyspeed
    enemy.setx(x)
    
    # move the enemy back and down
    if enemy.xcor() > 280:
        # move the enemy down
        y = enemy.ycor()
        y = y - 40
        if y < -250:
            print("Game Over")
            break
        enemy.sety(y)
        # change enemy direction
        enemyspeed = -1

    if enemy.xcor() < -280:
        # move the enemy down
        y = enemy.ycor()
        y = y - 40
        if y < -250:
            print("Game Over")
            break    
        enemy.sety(y)
            # change enemy direction
        enemyspeed = 1
        
    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
        
    if isCollision(bullet, enemy):
        # Reset the bullet
        bullet.hideturtle()
        bullet.setposition(0, -400)
        # Reset the enemy
        enemy.setposition(random.randint(-280, 280), 250)
        
    turtle.update()