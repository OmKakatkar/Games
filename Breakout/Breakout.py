import turtle

#Set the default window properties
window = turtle.Screen()
window.bgcolor("Black")
window.setup(500,500)
window.title("BREAKOUT")
window.tracer(0)


#Create a board
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.shapesize(stretch_wid=1,stretch_len=3) #Width = 10, Length = 30
board.pu()
board.goto(1.5,-230)                #Reference is bottom-right corner

#Create a ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.pu()
# delta change for ball
dx = 0.1
dy = -0.08

#Create a brick
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=2,stretch_len=3) #Width = 20, Length = 30
b.pu()
b.goto(-130,220)

def board_left():
    """
    Moves the board to left
    """
    x = board.xcor()
    if x >= -210:
        x -= 10
        board.setx(x)


def board_right():
    """
    Moves the board to right
    """
    x = board.xcor()
    if x <= 210:
        x += 10
        board.setx(x)

#Keyboard binding
window.listen()
window.onkeypress(board_left,"Left")
window.onkeypress(board_right,"Right")


while True:

    window.update()

    ball.sety(ball.ycor() + dy)
    ball.setx(ball.xcor() + dx)


    if ball.ycor() > 240:
        ball.sety(240)
        dy *= -1
        
    elif ball.ycor() <  -240:
        ball.goto(0,0)
        dy *= 1
            
    if ball.xcor() > 240:
        ball.setx(240)
        dx *= -1
        
    elif ball.xcor() < -240:
        ball.setx(-240)
        dx *= -1

    if (ball.ycor() < -220 and ball.ycor() >  -240)  and ((ball.xcor() < board.xcor() + 20) and (ball.xcor() > board.xcor() - 20)):
        ball.sety(-220)
        dy *= -1

    if b.isvisible() and (ball.ycor() < b.ycor() + 10 and ball.ycor() >= b.ycor()) and ((ball.xcor() < b.xcor() + 20) and (ball.xcor() > b.xcor() - 20)):
        b.ht()
        dy *= -1
    
window.mainloop()
