import tkinter
import random

X_MAX,Y_MAX=800,600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def stvorec(x,y,pocet,velkost,medzery=5):
    for a in range(pocet):
        canvas.create_rectangle(x-velkost/2,y-velkost/2,x+velkost/2,y+velkost/2)
        velkost=velkost-2*medzery

for b in range(10):
    velkost=random.randint(150,300)
    x,y=random.randint(round(velkost/2),X_MAX-round(velkost/2)),random.randint(round(velkost/2),Y_MAX-round(velkost/2))
    pocet=random.randint(5,11)
    stvorec(x,y,pocet,velkost,5)

        










