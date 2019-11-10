import tkinter
import random
X_MAX,Y_MAX=800,600
canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def vagon(x,y,farba,r=12):
    canvas.create_rectangle(x-10,y+42,x+110,y+45,fill="black")
    canvas.create_rectangle(x,y,x+100,y+50,fill=farba)
    canvas.create_oval(x+25-r,y+50-r,x+25+r,y+50+r,fill="black")
    canvas.create_oval(x+75-r,y+50-r,x+75+r,y+50+r,fill="black")

def vlak1():
    x=50
    for a in range(4):
        vagon(x,Y_MAX/3-100,"red",12)
        x=x+114

def vlak2():
    x=50
    for b in range(2):
        vagon(x,2*Y_MAX/3-100,"lime",12)
        x=x+114

def vlak3():
    x=50
    for c in range(3):
        vagon(x,Y_MAX-100,"blue",12)
        x=x+114

vlak1()
vlak2()
vlak3()
