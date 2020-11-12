import tkinter
import math
import sys
import sympy as sp
from PIL import Image, ImageTk
from gui import interfaz

input_text=str()
root = tkinter.Toplevel()
path1=#"file ubication"
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
r=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(r#"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="LAYERS METHOD")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    img_layers1=ImageTk.PhotoImage(Image.open(path1))
    layers=tkinter.Label(root,image=img_layers1,height=200,width=520)
    layers.place(x=50, y=100)

    entrya = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=var, insertwidth=10, bg="white", justify="right")
    entrya.place(x=200, y=350)
    lbla = tkinter.Label(root, text="A= ", width=width_label, height=height_label)
    lbla.place(x=75, y=352)
    v=entrya
    global v

    entryb = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entryb.place(x=200, y=420)
    lblb = tkinter.Label(root, text="B= ", width=width_label, height=height_label)
    lblb.place(x=75, y=422)
    y=entryb
    global y

    entrypx = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=date, insertwidth=10, bg="white", justify="right")
    entrypx.place(x=200, y=490)
    lblpx = tkinter.Label(root, text="rh= ", width=width_label, height=height_label)
    lblpx.place(x=75, y=492)
    z=entrypx
    global z

    entryhx = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=elemento, insertwidth=10, bg="white", justify="right")
    entryhx.place(x=200, y=560)
    lblhx = tkinter.Label(root, text="rh= ", width=width_label, height=height_label)
    lblhx.place(x=75, y=562)
    r=entryhx
    global r

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_layers)
    buttoncalculate.place(x=250, y=630)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=690)
    lbltotal = tkinter.Label(root, text="TOTAL= ", width=widht_label, height=height_label)
    lbltotal.place(x=75, y=692)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=730)

    root.mainloop()

def regresar():
    interfaz.create_frame()

def vol_layers():
    x=sp.Symbol('x')
    px=float(z.get())
    hx=float(r.get())
    a=float(v.get())
    b=float(y.get())
    fx=px*hx
    dx= sp.integrate(fx, (x, a, b)).doit()*2*math.pi
    tot=str(dx)
    result.set(tot)

