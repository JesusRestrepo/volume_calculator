import tkinter
import math
import sys
from PIL import Image, ImageTk
from gui import interfaz

input_text=str()
root = tkinter.Toplevel()
path1=#"file ubication"
width_label = 15
height_label = 2
result=tkinter.StringVar()
mystring=tkinter.StringVar(root)
x=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(os.path.join(sys.path[0], #"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="SPHERE VOLUME")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    text=tkinter.Label(root,text="SPHERE VOLUME= 4/3π*R^3")
    text.pack(anchor="center")
    
    img_sphere=ImageTk.PhotoImage(Image.open(path1))
    sphere=tkinter.Label(root,image=img_sphere,height=400,width=430)
    sphere.place(x=150, y=100)

    entryR = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entryR.place(x=200, y=500)
    lblR = tkinter.Label(root, text="R= ", width=width_label, height=height_label)
    lblR.place(x=75, y=502)
    x=entryR
    global x

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_sphere)
    buttoncalculate.place(x=250, y=570)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=640)
    lbltotal = tkinter.Label(root, text="TOTAL= ", width=width_label, height=height_label)
    lbltotal.place(x=75, y=642)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=700)

    root.mainloop()

def regresar():
    interfaz.create_frame()

def vol_sphere():
    r=int(x.get())
    volume_sphere=(4/3)*math.pi*r**3
    result.set(volume_sphere)

