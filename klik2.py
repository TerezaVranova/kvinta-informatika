import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

xx,yy=0,0

def klik(event):
    x,y=event.x,event.y
    r=5
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="red")
    global xx,yy
    xx,yy=x,y
    
def pusti(event):
    x,y=event.x,event.y
    r=5
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue")
    canvas.create_line(xx,yy,x,y)
     
canvas.bind("<ButtonPress>",klik)
canvas.bind("<ButtonRelease>",pusti)
