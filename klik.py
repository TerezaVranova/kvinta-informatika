import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

def klik(event):
    x,y=event.x,event.y
    r=5
    canvas.create_oval(x+r,y+r,x-r,y-r,outline="black",fill="black")

def pohyb(event):
    x,y=event.x,event.y
    r=5
    canvas.create_oval(x+r,y+r,x-r,y-r,outline="blue",fill="blue")

canvas.bind("<ButtonPress>",klik)
canvas.bind("<Motion>",pohyb)
    
    
