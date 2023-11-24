import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by HTL")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('purple')
paddle_a.penup()
paddle_a.goto(-300, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('purple')
paddle_b.penup()
paddle_b.goto(292, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('purple')
ball.penup()
ball.goto(0, 0)
# separate move to x and y
ball.dx = 0.05
ball.dy = 0.05

# score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"A {score_a}  VS  {score_b} B", align='center', font=('Courier', 24, 'normal'))


# Move
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)


# binding keyboard
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('ball-hit-wall.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('ball-hit-wall.wav', winsound.SND_ASYNC)

    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound('losing-point.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"A {score_a}  VS  {score_b} B", align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound('losing-point.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"A {score_a}  VS  {score_b} B", align='center', font=('Courier', 24, 'normal'))

    # Paddle and Ball collisions
    if 280 > ball.xcor() > 270 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound('ball-hit-paddle.wav', winsound.SND_ASYNC)

    if -290 < ball.xcor() < -280 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound('ball-hit-paddle.wav', winsound.SND_ASYNC)
