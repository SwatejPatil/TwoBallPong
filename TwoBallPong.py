# Pong Game in Python using Turtle
#Importing Important Libraries
import turtle
import os

#Main Game Window
window = turtle.Screen()
window.title("TwoBallPong")
window.bgcolor("black")
window.setup(width=800, height=900)
window.tracer(0)

#Scores 
score_a = 0
score_b = 0

#Player 1 Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=7,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#Player 2 Paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid=7,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


#Ball 1
ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.shape("circle")
ball_1.color("yellow")
ball_1.penup()
ball_1.goto(0, 0)
ball_1.dx = 0.5
ball_1.dy = 0.5

#Ball 2
ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.shape("circle")
ball_2.color("cyan")
ball_2.penup()
ball_2.goto(0, 0)
ball_2.dx = -0.5
ball_2.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))




#Moveing Paddle Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 30
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 30
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 30
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 30
    paddle_2.sety(y)

# Keypress Inputs
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")


#Main Game Loop
while True:
    window.update()

    # Ball_1 Movement
    ball_1.setx(ball_1.xcor() + ball_1.dx)
    ball_1.sety(ball_1.ycor() + ball_1.dy)

    # Ball_2 Movement
    ball_2.setx(ball_2.xcor() + ball_2.dx)
    ball_2.sety(ball_2.ycor() + ball_2.dy)

# Border checking

    # Top and Bottom
    #Ball_1
    if ball_1.ycor() > 290:
        ball_1.sety(290)
        ball_1.dy *= -1

    elif ball_1.ycor() < -290:
        ball_1.sety(-290)
        ball_1.dy *= -1

    # Top and Bottom
    #Ball_2
    if ball_2.ycor() > 290:
        ball_2.sety(290)
        ball_2.dy *= -1

    elif ball_2.ycor() < -290:
        ball_2.sety(-290)
        ball_2.dy *= -1


    # Left and right
    #Ball_1
    if ball_1.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball_1.goto(0, 0)
        ball_1.dx *= -1

    elif ball_1.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball_1.goto(0, 0)
        ball_1.dx *= -1

    # Left and right
    #Ball_2
    if ball_2.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball_2.goto(0, 0)
        ball_2.dx *= -1

    elif ball_2.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball_2.goto(0, 0)
        ball_2.dx *= -1




    # Paddle and ball_1 collisions
    if ball_1.xcor() < -340 and ball_1.ycor() < paddle_1.ycor() + 50 and ball_1.ycor() > paddle_1.ycor() - 50:
        ball_1.dx *= -1

    elif ball_1.xcor() > 340 and ball_1.ycor() < paddle_2.ycor() + 50 and ball_1.ycor() > paddle_2.ycor() - 50:
        ball_1.dx *= -1

    # Paddle and ball_2 collisions
    if ball_2.xcor() < -340 and ball_2.ycor() < paddle_1.ycor() + 50 and ball_2.ycor() > paddle_1.ycor() - 50:
        ball_2.dx *= -1

    elif ball_2.xcor() > 340 and ball_2.ycor() < paddle_2.ycor() + 50 and ball_2.ycor() > paddle_2.ycor() - 50:
        ball_2.dx *= -1
