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

def flotila():
    a=0
    x=500-100*a
    for a in range(1,4):
        x=500-100*a
        lodka(x,200,a)

def obraz():
    vlajka(-50,275,"darkgreen")
    vlajka(480,275,"red")
    more()
    mesiac(175,100,"darkgreen","red",30)
    odraz()
    logo(705,100,20,"light sky blue","red")
    #flotila()

def mesiacmesiac():
    y=300
    for i in range(1000):
        canvas.delete("all")
        obraz()
        odraz(500,y,40)
        y-=1
        canvas.update()
        canvas.after(10)

#mesiacmesiac()

def lodky():
    m=500
    n=400
    o=300
    for i in range(1,1001):
        canvas.delete("all")
        obraz()
        lodka(o,200,1)
        lodka(n,200,2)
        lodka(m,200,3)
        m+=10
        n+=8
        o+=6
        canvas.update()
        canvas.after(10)

lodky()
