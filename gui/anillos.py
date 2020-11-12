import tkinter
import math
import sys
import sympy as sp
from PIL import Image, ImageTk
from gui import interfaz

input_text=str()
root = tkinter.Toplevel()
path1=#"file ubication"
path2=#"file ubication"
width_label = 15
height_label = 2
var=tkinter.StringVar(root)
mystring=tkinter.StringVar(root)
date=tkinter.StringVar(root)
elemento=tkinter.StringVar(root)
result=tkinter.StringVar()
v=None
y=None
z=None
b=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(r#"file ubication".ico)
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="RINGS METHOD")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    img_rings1=ImageTk.PhotoImage(Image.open(path1))
    rings=tkinter.Label(root,image=img_rings1,height=200,width=300)
    rings.place(x=150, y=100)

    entryRx = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=date, insertwidth=10, bg="white", justify="right")
    entryRx.place(x=200, y=350)
    lblRx = tkinter.Label(root, text="Rx= ", width=width_label, height=height_label)
    lblRx.place(x=75, y=352)
    v=entryRx
    global v

    entryrx = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=var, insertwidth=10, bg="white", justify="right")
    entryrx.place(x=200, y=420)
    lblrx = tkinter.Label(root, text="rx= ", width=width_label, height=height_label)
    lblrx.place(x=75, y=422)
    y=entryrx
    global y

    entrya = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entrya.place(x=200, y=490)
    lbla = tkinter.Label(root, text="A= ", width=width_label, height=height_label)
    lbla.place(x=75, y=492)
    z=entrya
    global z

    entryb = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=elemento, insertwidth=10, bg="white", justify="right")
    entryb.place(x=200, y=560)
    lblb = tkinter.Label(root, text="B= ", width=width_label, height=height_label)
    lblb.place(x=75, y=562)
    b=entryb
    global b

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_ring)
    buttoncalculate.place(x=250, y=620)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=660)
    lbltotal = tkinter.Label(root, text="TOTAL= ", width=width_label, height=height_label)
    lbltotal.place(x=75, y=662)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=700)

    root.mainloop()

def regresar():
    interfaz.create_frame()

def vol_ring():
    x=sp.Symbol('x')
    a=float(z.get())
    p=float(b.get())
    Rx=float(v.get())
    rx=float(y.get())
    fx=Rx**2-rx**2
    dx= sp.integrate(fx, (x, a, p)).doit()*math.pi
    tot=str(dx)
    result.set(tot)