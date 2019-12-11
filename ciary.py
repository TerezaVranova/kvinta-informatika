import tkinter
from random import randrange, randint
x_max,y_max=600,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

s1,s2=x_max/2,y_max/2

for i in range(2000):
    x,y=randint(0,x_max),randint(0,y_max)
    if x>=x_max/2 and y>=y_max/2:
        farba="green"
    elif x>=x_max/2 and y<=y_max/2:
        farba="blue"
    elif x<=x_max/2 and y<=y_max/2:
        farba="red"
    elif x<=x_max/2 and y>=y_max/2:
        farba="yellow"
    else:
        print("chyba v matrixe")
    canvas.create_line(s1,s2,x,y,fill=farba)
