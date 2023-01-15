from turtle import *
color('red','cyan')
begin_fill()

def draw_square(c):
    penup()
    goto(c)
    pendown()
    for i in range(4):
        forward(100)
        right(90)

def draw_x(c):
    penup()
    goto(c)
    pendown()
    for i in range(4):
        forward(100)
        right(90)


T2 = [[(0,0), (100,0), (200,0)],[(0,100), (100,100), (200,100)], [(0,200), (100,200), (200,200)]]

for r in T2:
   for c in r:
       draw_square(c)

done()
