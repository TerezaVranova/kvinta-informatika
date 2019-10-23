import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def stvorec(x,y,pocet,r,medzery):
    for a in range(pocet):
        canvas.create_rectangle(x-r,y-r,x+r,y+r)
        r=r-medzery

for b in range(10):
    stvorec(random.randint(0,800),random.randint,10,100,10)
    
