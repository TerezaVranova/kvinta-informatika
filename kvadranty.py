import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

r=20
x,y=randint(r,x_max-r),randint(r,y_max-r)
farba="black"

for i in range(2000):
    x,y=randint(r,x_max-r),randint(r,y_max-r)
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
    canvas.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)
