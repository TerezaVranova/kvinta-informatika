import tkinter
canvas=tkinter.Canvas(width=800,height=700,background="white")
canvas.pack()
import random

def strom(x,y,r):
    canvas.create_rectangle(x,y,x+20,y+120,fill="brown",outline="brown")
    canvas.create_oval(x+10-r,y-r,x+10+r,y+r,fill="lime")

for a in range(10):
    x,y,r=random.randint(0,800),random.randint(0,700),random.randint(30,80)
    strom(x,y,r)

def trava(x,y,m,n):
    x,y=random.randint(0,800),random.randint(0,700)
    for b in range(3,11):
        m,n=random.randint(-30,30),random.randint(-30,-5)
        canvas.create_line(x,y,x+m,y+n,fill="green",width=2)

for c in range(20):
    x,y,m,n=random.randint(0,800),random.randint(0,700),random.randint(-30,30),random.randint(-50,-5)
    trava(x,y,m,n)
