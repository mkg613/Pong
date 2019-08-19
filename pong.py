import turtle

win = turtle.Screen()
win.title("Pong by mkg613")
win.bgcolor("lime green")
win.setup(width=800, height=600)
win.tracer(0)

#Paddle1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=6,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#Paddle2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=6,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)


#Pingpong
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)


#Function
def paddle_1_up():  #define function
    y = paddle_1.ycor()
    y +=20
    paddle_1.sety(y)

def paddle_1_down():  
    y = paddle_1.ycor()
    y -=20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y +=20
    paddle_2.sety(y)
    
def paddle_2_down():  
    y = paddle_2.ycor()
    y -=20
    paddle_2.sety(y)


#Keyboard Binding
win.listen()    #listen for keyboard inputs
win.onkeypress(paddle_1_up,"w")
win.onkeypress(paddle_1_down,"s")
win.onkeypress(paddle_2_up,"Up")
win.onkeypress(paddle_2_down,"Down")

#Main Game Loop
while True:
    win.update()
    
