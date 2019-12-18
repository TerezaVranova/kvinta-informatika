import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

xx,yy=0,0

def kreslenie(event):
    x,y=event.x,event.y
    r=1
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="black")
    global xx,yy
    xx,yy=x,y

x1,y1=0,0
def kreslenie2(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=2)
    x1,y1=x,y

#canvas.bind("<ButtonPress>",)
canvas.bind("<Motion>",kreslenie2)
#canvas.bind("<ButtonRelease>",)

    
