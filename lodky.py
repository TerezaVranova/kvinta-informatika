import tkinter
canvas=tkinter.Canvas(width=800,height=600,background="white")
canvas.pack()
import random

def more():
    canvas.create_rectangle(0,300,800,600,fill="blue")

def mesiac(x=500,y=random.randint(50,170),pozadie="white",farba="yellow",r=40):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x+r*0.65-r,y-r,x+r*0.65+r,y+r,fill=pozadie,outline=pozadie)

def odraz(x=500,y=random.randint(50,170),r=40):
    mesiac(x,y,"white","yellow",r)
    mesiac(x,600-y,pozadie="blue",farba="yellow",r=40)

def vlajka(x,y,farba="darkgreen"):
    canvas.create_oval(x,y,x+300,y+300,fill="brown")
    canvas.create_line(x+150,50,x+150,y)
    canvas.create_rectangle(x+150,50,x+300,150,fill=farba)

def mesiac_obrateny(x,y,pozadie="white",farba="yellow",r=50):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x-r*0.65-r,y-r,x-r*0.65+r,y+r,fill=pozadie,outline=pozadie)

def logo(x,y,r=50,farba="light sky blue",pozadie="red"):
    mesiac(x+r*1.125,y,pozadie,farba,r)
    mesiac_obrateny(x-r*1.125,y,pozadie,farba,r)

def lodka(x,y,velkost):
    a=10
    b=100
    r=8
    canvas.create_rectangle(x,y,x+velkost*a,y+velkost*b,fill="brown",outline="brown")
    canvas.create_polygon(x+velkost*a/2,y,x+velkost*3*a,y+velkost*b/2,x+velkost*a/2,y+velkost*b*2/3,fill="white",outline="black")
    canvas.create_polygon(x-velkost*b/2,y+velkost*b*3/4,x+velkost*b/2+velkost*a,y+velkost*b*3/4,x+velkost*b/4+velkost*a,y+velkost*b,x-velkost*b/4,y+velkost*b,fill="saddle brown",outline="black")
    logo(x+velkost*a/2,y+velkost*b*7/8,r*velkost,farba="light sky blue",pozadie="saddle brown")

vlajka(-50,275,"darkgreen")
vlajka(480,275,"red")
more()
odraz()
mesiac(175,100,"darkgreen","red",30)
logo(705,100,20,"light sky blue","red")

for a in range(1,4):
    lodka(500-100*a,200,a)
