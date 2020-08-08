import turtle

#Create window and setup
win = turtle.Screen()
win.bgcolor("Black")
win.setup(800,600)
win.title("PING PONG")
win.tracer(0)

#Create paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_a.pu()
paddle_a.goto(-370,0)

#Create paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_b.pu()
paddle_b.goto(360,0)

#Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.pu()
ball.dx = 0.3
ball.dy = 0.3

#Create Pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.pu()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 24, "normal"))

#Check borders for ball
def borderCheck():
    borderX = 380
    borderY = 280
    if ball.ycor() > borderY + 10:
        ball.sety(borderY + 10)
        ball.dy = -ball.dy
        
    if ball.ycor() < -borderY:
        ball.sety(-borderY)
        ball.dy = -ball.dy
    
    if ball.xcor() < -borderX - 10:
        ball.goto(0,0)
        ball.dx = -ball.dx
        pen.clear()

    if ball.xcor() > borderX:
        ball.goto(0,0)
        ball.dx = -ball.dx

#Colliding ball with paddle_a
def paddle_a_check():
    if (ball.xcor() < -360 and ball.xcor() > -370 ) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-360)
        ball.dx = -ball.dx

#Colliding ball with paddle_b
def paddle_b_check():
    if (ball.xcor() > 350 and ball.xcor() < 360 ) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): 
        ball.setx(350)
        ball.dx = -ball.dx
        
#Moving both paddles
def paddle_a_up():
    if paddle_a.ycor() < 260:
        paddle_a.sety(paddle_a.ycor() + 10)

def paddle_a_dn():
    if paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - 10)

def paddle_b_up():
    if paddle_b.ycor() < 260:
        paddle_b.sety(paddle_b.ycor() + 10)

def paddle_b_dn():
    if paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - 10)

#Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_dn, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_dn, "Down")

while True:


    #Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    borderCheck()
    paddle_a_check()
    paddle_b_check()

    #Autopilot
    #paddle_a.sety(ball.ycor())     
    #paddle_b.sety(ball.ycor())
    
win.done()
