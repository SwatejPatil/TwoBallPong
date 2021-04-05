# Pong Game in Python using Turtle
#Importing Important Libraries
import turtle

#Main Game Window
window = turtle.Screen()
window.title("TwoBallPong")
window.bgcolor("black")
window.setup(width=800, height=900)
window.tracer(0)

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
ball_1.dx = 2
ball_1.dy = 2



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

