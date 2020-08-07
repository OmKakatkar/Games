import turtle

#Create window and setup
win = turtle.Screen()
win.bgcolor("Black")
win.setup(800,600)
win.title("PING PONG")
win.tracer(0)

#Create paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_a.pu()
paddle_a.goto(-370,0)

#Create paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_b.pu()
paddle_b.goto(360,0)

#Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.pu()
ball.dx = 0.5
ball.dy = 0.5

def borderCheck():
    borderX = 380
    borderY = 280
    if ball.ycor() > borderY:
        ball.sety(borderY)
        ball.dy = -ball.dy
        
    if ball.ycor() < -borderY:
        ball.sety(-borderY)
        ball.dy = -ball.dy
    
    if ball.xcor() < -borderX:
        ball.setx(-borderX)
        ball.dx = -ball.dx

    if ball.xcor() > borderX:
        ball.setx(borderX)
        ball.dx = -ball.dx

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

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_dn, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_dn, "Down")
while True:
    win.update()

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    borderCheck()
    
win.done()
