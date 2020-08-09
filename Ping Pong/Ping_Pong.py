import turtle
import winsound

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
paddle_a.goto(-370,-250)

#Create paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_b.pu()
paddle_b.goto(360,260)

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

score_a = 0
score_b = 0

paddleMove = 30

running = True

#Check borders for ball
def borderCheck():
    borderX = 380
    borderY = 280
    global score_a,score_b
    
    if ball.ycor() > borderY + 10:
        ball.sety(borderY + 10)
        ball.dy = -ball.dy
        winsound.PlaySound("ping-pong-ball-hit-wall.wav", winsound.SND_ASYNC)
            
    if ball.ycor() < -borderY:
        ball.sety(-borderY)
        ball.dy = -ball.dy
        winsound.PlaySound("ping-pong-ball-hit-wall.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -borderX - 10:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_b += 1
        score_update()
        
    if ball.xcor() > borderX:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_a += 1
        score_update()
        
#Colliding ball with paddle_a
def paddle_a_check():
    if (ball.xcor() < -360 and ball.xcor() > -370 ) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-360)
        ball.dx = -ball.dx
        winsound.PlaySound("ping-pong-ball-hit-paddle.wav", winsound.SND_ASYNC)

#Colliding ball with paddle_b
def paddle_b_check():
    if (ball.xcor() > 350 and ball.xcor() < 360 ) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): 
        ball.setx(350)
        ball.dx = -ball.dx
        winsound.PlaySound("ping-pong-ball-hit-paddle.wav", winsound.SND_ASYNC)
        
#Moving paddle A Up
def paddle_a_up():
    running == True
    if paddle_a.ycor() < 270 - paddleMove:
        paddle_a.sety(paddle_a.ycor() + paddleMove)

#Moving paddle A Down
def paddle_a_dn():
    running == True
    if paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - paddleMove)

#Moving paddle B Up
def paddle_b_up():
    running == True
    if paddle_b.ycor() < 270 - paddleMove:
        paddle_b.sety(paddle_b.ycor() + paddleMove)

#Moving paddle B Down
def paddle_b_dn():
    running == True
    if paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - paddleMove)

#Updating Score
def score_update():
    global score_a,score_b
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

##def game_pause():
##    global running
##    running == False

#Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_dn, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_dn, "Down")

##win.onkeypress(game_pause,"p")

while running:

    win.update()
    
    #Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #paddle_a.sety(paddle_a.ycor() + 10)
    #paddle_b.sety(paddle_a.ycor() + 10)
    
    borderCheck()
    paddle_a_check()
    paddle_b_check()

    #Autopilot
    #paddle_a.sety(ball.ycor())     
    #paddle_b.sety(ball.ycor())

    if score_a == 5:
        pen.clear()
        pen.goto(0,0)
        pen.write("Player A Wins!!!", align="center", font=("Courier", 40, "normal"))
        winsound.PlaySound("applause.wav",winsound.SND_FILENAME)
        pen.clear()
        score_a = 0
        score_b = 0
        pen.goto(0,260)
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        
    elif score_b == 5 :
        pen.clear()
        pen.goto(0,0)
        pen.write("Player B Wins!!!", align="center", font=("Courier", 40, "normal"))
        winsound.PlaySound("applause.wav",winsound.SND_FILENAME)
        pen.clear()
        score_a = 0
        score_b = 0
        pen.goto(0,260)
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

win.done()
