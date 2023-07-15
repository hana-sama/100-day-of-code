import turtle

wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.tracer(0)
wn.bgcolor('black')

bottom_left = turtle.Turtle()
bottom_left.shape('circle')
bottom_left.color('white')
bottom_left.shapesize(stretch_wid=5, stretch_len=5)
bottom_left.penup()
bottom_left.goto(-250, -250)


while True:
    wn.update()