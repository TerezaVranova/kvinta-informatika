import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

x1,y1=0,0

def klik(event):
    x,y=event.x,event.y

def kreslenie(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=2)
    x1,y1=x,y

#canvas.bind("<ButtonPress>",klik)
canvas.bind("<Motion>",kreslenie)
#canvas.bind("<ButtonRelease>",)

    
