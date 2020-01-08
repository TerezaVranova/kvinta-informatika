import tkinter
from random import randrange,randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

r=50
x,y=randint(r,x_max-r),r+randrange(y_max-2*r)
dx=3
dy=3

while True:
    canvas.delete("all")
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue")
    x+=dx
    y+=dy
    if x>=x_max-r or x<=r:
        dx*=-1
    if y>=y_max-r or y<=r:
        dy*=-1
    canvas.update()
    canvas.after(1)
