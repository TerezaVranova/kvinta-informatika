import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

r=10
farba="yellow"
for i in range(20000):
    x,y=randint(0,x_max),randint(0,y_max)
    if x>=x_max*2/6 and y>=y_max*3/5:
        farba="blue"
    elif x>=x_max*2/6 and y<=y_max*2/5:
        farba="blue"
    elif x<=x_max*1/6 and y<=y_max*2/5:
        farba="blue"
    elif x<=x_max*1/6 and y>=y_max*3/5:
        farba="blue"
    else:
        farba="yellow"
    canvas.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)
        
