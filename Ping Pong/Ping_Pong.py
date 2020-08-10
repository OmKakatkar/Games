"""
Ping Pong Game Version 2.0
Windows Compatible.
by Om Kakatkar

This is a basic version of Ping Pong Game made in Turtle Module.
There are 3 screens currently. (Start, Actual Game, End)
"""

import turtle
import winsound
import time

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
ball.dx = 250
ball.dy = 250

#Create Pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.pu()
pen.goto(0,260)

#Initial scored of Player A and Player B
score_a = 0
score_b = 0

#No. of spaces paddles move up or down
paddleMove = 30

game_state = "Start_Screen"

is_paused = False

def borderCheck():
    """
    Checks the distance of ball wrt border of window.
    If the ball is colliding to upper or lower boundary, a sound plays and
    the y direction of ball is flipped.
    If the ball is colliding to left or right boundary, a sound plays and
    the ball is reset to home or position 0,0 as per the turtle module.
    It also updates the scores of the players when the ball touches the opponent's
    boundary.
    The X and Y border limits are specified in borderX and borderY respectively.
    Global variables score_a and score_b are used to update the score.
    This function calls another function score_update to update the scores.
    """
    borderX = 380
    borderY = 280
    global score_a,score_b
    
    if ball.ycor() > borderY + 10:
        ball.sety(borderY + 10)
        ball.dy = -ball.dy
        winsound.PlaySound("Sounds/ping-pong-ball-hit-wall.wav", winsound.SND_ASYNC)
            
    if ball.ycor() < -borderY:
        ball.sety(-borderY)
        ball.dy = -ball.dy
        winsound.PlaySound("Sounds/ping-pong-ball-hit-wall.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -borderX - 10:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_b += 1
        win.ontimer(score_update(),500)
        
    if ball.xcor() > borderX:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_a += 1
        win.ontimer(score_update(),500)
                
def paddle_a_check():
    """
    Checks the position of the ball wrt paddle_a.
    If the ball is colliding with the paddle_a, the x and y coordinates are
    reversed and a sound is played.
    """
    if (ball.xcor() < -360 and ball.xcor() > -370 ) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-360)
        ball.dx = -ball.dx
        winsound.PlaySound("Sounds/ping-pong-ball-hit-paddle.wav", winsound.SND_ASYNC)

def paddle_b_check():
    """
    Checks the position of the ball wrt paddle_b.
    If the ball is colliding with the paddle_b, the x and y coordinates are
    reversed and a sound is played.
    """
    if (ball.xcor() > 350 and ball.xcor() < 360 ) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): 
        ball.setx(350)
        ball.dx = -ball.dx
        winsound.PlaySound("Sounds/ping-pong-ball-hit-paddle.wav", winsound.SND_ASYNC)
        
def paddle_a_up():
    """
    Moves paddle_a up if "w" key is pressed.
    If the paddle is colliding with the upper boundary, the paddle does not
    move further up.
    """
    if paddle_a.ycor() < 270 - paddleMove:
        paddle_a.sety(paddle_a.ycor() + paddleMove)

def paddle_a_dn():
    """
    Moves paddle_a down if "s" key is pressed.
    If the paddle is colliding with the lower boundary, the paddle does not
    move further down.
    """
    if paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - paddleMove)

def paddle_b_up():
    """
    Moves paddle_b up if "Up" arrow key is pressed.
    If the paddle is colliding with the upper boundary, the paddle does not
    move further up.
    """
    if paddle_b.ycor() < 270 - paddleMove:
        paddle_b.sety(paddle_b.ycor() + paddleMove)

def paddle_b_dn():
    """
    Moves paddle_b down if "Down" arrow key is pressed.
    If the paddle is colliding with the lower boundary, the paddle does not
    move further down.
    """
    if paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - paddleMove)

#Updating Score
def score_update():
    """
    This function uses global variables score_a and score_b to update the score
    on the screen.
    A turtle called pen is used to write the score on the screen.
    """
    global score_a,score_b
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

def game_start():
    global game_state
    pen.clear()
    pen.goto(0,260)
    score_update()
    paddle_a.st()
    paddle_b.st()
    ball.st()
    
    if game_state == "Start_Screen":
        game_state = "Run"
        win.bgpic("nopic")
        pen.color("white")        
        #winsound.PlaySound("Sounds/whistle_blow_short.mp3", winsound.SND_FILENAME)

    elif game_state == "Game_Over":
        paddle_a.goto(-370,-250)
        paddle_b.goto(360,260)
        ball.goto(0,0)
        game_state = "Run"   
        
def game_end():
    if game_state == "Game_Over":
        win.bye()
    
#incomplete
def toggle_pause():
    global is_paused
    if game_state == "Run":
        if is_paused == True:
            is_paused = False
        else:
            is_paused = True

#Keyboard binding
win.listen()

win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_up, "w")

win.onkeypress(paddle_a_dn, "s")
win.onkeypress(paddle_a_dn, "S")

win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_dn, "Down")

win.onkeypress(toggle_pause,"x")
win.onkeypress(toggle_pause,"X")

win.onkeypress(game_start, "y")
win.onkeypress(game_start, "Y")

win.onkeypress(game_end, "n")
win.onkeypress(game_end, "N")


#try:
while True:
    
    if game_state == "Start_Screen":
        win.bgpic("Images/start_game2.gif")
        paddle_a.ht()
        paddle_b.ht()
        ball.ht()
        pen.clear()
        pen.goto(0,200)
        pen.color("black")
        pen.write("Press 'Y' to Start. ", align="center", font=("Arial", 30, "italic"))
        last_time = time.perf_counter()
        
    elif game_state == "Run":

        if not is_paused:
        
            score_update()
            
            #Calculating the time elapsed between two iterations of the loop
            current_time = time.perf_counter()
            elapsed_time = current_time - last_time
            last_time = current_time

            #Move the ball
            ball.sety(ball.ycor() + ball.dy * elapsed_time)
            ball.setx(ball.xcor() + ball.dx * elapsed_time)

            #Moves the paddle till the border in the direction specified by the keys
            #Incomplete implementation
            #paddle_a.sety(paddle_a.ycor() + 10)
            #paddle_b.sety(paddle_a.ycor() + 10)

            #Check all conditons     
            borderCheck()
            paddle_a_check()
            paddle_b_check()

            #Autopilot
            #paddle_a.sety(ball.ycor())     
            #paddle_b.sety(ball.ycor())

            #Check the winner    
            if score_a == 3:
                pen.clear()
                pen.goto(0,0)
                pen.write("Player A Wins!!!", align="center", font=("Courier", 40, "bold"))
                winsound.PlaySound("Sounds/applause.wav",winsound.SND_FILENAME)
                pen.clear()
                score_a = 0
                score_b = 0
                pen.goto(0,260)
                game_state = "Game_Over"
                
            elif score_b == 3 :
                pen.clear()
                pen.goto(0,0)
                pen.write("Player B Wins!!!", align="center", font=("Courier", 40, "bold"))
                winsound.PlaySound("Sounds/applause.wav",winsound.SND_FILENAME)
                pen.clear()
                score_a = 0
                score_b = 0
                pen.goto(0,260)
                game_state = "Game_Over"

        elif is_paused :
            print("Paused")
            pass
            
    elif game_state == "Game_Over":
        paddle_a.ht()
        paddle_b.ht()
        ball.ht()
        pen.clear()
        pen.goto(0,-50)
        pen.write("GAME OVER \n Play Again?\n       Y / N", align = "center",font = ("Arial",40,"bold"))
        last_time = time.perf_counter()
        
    win.update()
    
win.done()
#except Exception:
 #   pass
