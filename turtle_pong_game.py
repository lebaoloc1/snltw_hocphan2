import turtle

wd_width = 800
wd_height = 600

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=wd_width, height=wd_height)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    
    pen.clear()
    pen.write(f"Player A: {score_a}\t\tPlayer B: {score_b}", align="center", font=("Courier", 24, "normal"))

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > (wd_height/2 - 10):
        ball.sety(wd_height/2 - 10)
        ball.dy *= -1

    if ball.ycor() < (-wd_height/2 + 10):
        ball.sety(-wd_height/2 + 10)
        ball.dy *= -1

    if ball.xcor() > paddle_b.xcor() - 20 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(paddle_b.xcor() - 20) 
        ball.dx *= -1
    elif ball.xcor() >= paddle_b.xcor() + 10:
        score_a += 1
        ball.goto(0, 0)

    if ball.xcor()  < paddle_a.xcor() + 20 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
        ball.setx(paddle_a.xcor() + 20)
        ball.dx *= -1
    elif ball.xcor() <= paddle_a.xcor() - 10:
        score_b += 1
        ball.goto(0, 0)
    