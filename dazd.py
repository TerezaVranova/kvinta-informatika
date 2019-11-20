import tkinter
canvas=tkinter.Canvas(width=800,height=600,background="white")
canvas.pack()
import random

def kvapka(x,y):
    canvas.create_oval(x,y,x+10,y+10,fill="#00ffff")

for i in range(1000):
    canvas.delete("all")
    for j in range(200):
        kvapka(random.randint(1,800),random.randint(1,600))
    canvas.update()
    canvas.after(50)
