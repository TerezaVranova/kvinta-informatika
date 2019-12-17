import tkinter
from random import randrange,randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

def symetria(event):
    x,y=event.x,event.y
    r=3
    a=x_max-x
    b=y_max-y
    m,n,o,p="blue","green","yellow","red"
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=m,outline=m)
    canvas.create_oval(a-r,b-r,a+r,b+r,fill=n,outline=n)
    canvas.create_oval(x-r,b-r,x+r,b+r,fill=o,outline=o)
    canvas.create_oval(a-r,y-r,a+r,y+r,fill=p,outline=p)
       
canvas.bind('<Motion>',symetria)
