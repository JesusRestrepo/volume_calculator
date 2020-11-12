import tkinter
import sys
from PIL import Image,ImageTk
from gui import cubo, esfera, cilindro, piramide, cono, anillos, capas
from tkinter import messagebox

root = tkinter.Toplevel()
width_botton=15
height_botton=2
width_image=128
height_image=128
path1=#"file ubication"
path2=#"file ubication"
path3=#"file ubication"
path4=#"file ubication"
path5=#"file ubication"
path6=#"file ubication"
path7=#"file ubication"

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(os.path.join(sys.path[0], #"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    messagebox.showinfo(message="WELCOME TO THE VOLUME CALCULATOR", title="VOLUME CALCULATOR")

    lbl=tkinter.Label(root,text="CHOOSE THE VOLUME TO FIND: ")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    img_cube=ImageTk.PhotoImage(Image.open(path1))
    cub=tkinter.Label(root,image=img_cube,height=height_image,width=width_image)
    cub.place(x=21,y=50)
    button_cube=tkinter.Button(root,text='CUBE',height=height_botton,width=width_botton, command=cu)
    button_cube.place(x=15,y=200)

    img_sphere=ImageTk.PhotoImage(Image.open(path2))
    spher=tkinter.Label(root,image=img_sphere,height=height_image,width=width_image)
    spher.place(x=241,y=50)
    button_sphere=tkinter.Button(root,text='SPHERE',height=height_botton,width=width_botton, command=es)
    button_sphere.place(x=235,y=200)

    img_cylinder=ImageTk.PhotoImage(Image.open(path3))
    cylind=tkinter.Label(root,image=img_cylinder,height=height_image,width=width_image)
    cilind.place(x=451,y=50)
    button_cylinder=tkinter.Button(root,text='CYLINDER',height=height_botton,width=width_botton, command=ci)
    button_cylinder.place(x=445,y=200)

    img_piyramid=ImageTk.PhotoImage(Image.open(path4))
    pyramid=tkinter.Label(root,image=img_pyramid,height=height_image,width=width_image)
    pyramid.place(x=21,y=300)
    button_pyramid=tkinter.Button(root,text='PYRAMID',height=height_botton,width=width_botton, command=pi)
    button_pyramid.place(x=15,y=450)

    img_cone=ImageTk.PhotoImage(Image.open(path5))
    con=tkinter.Label(root,image=img_cone,height=height_image,width=width_image)
    con.place(x=241,y=300)
    button_cone=tkinter.Button(root,text='CONE',height=height_botton,width=width_botton, command=co)
    button_cone.place(x=235,y=450)

    img_rings=ImageTk.PhotoImage(Image.open(path6))
    ring=tkinter.Label(root,image=img_rings,height=height_image,width=width_image)
    ring.place(x=451,y=300)
    button_ring=tkinter.Button(root,text='RINGS METHOD',height=height_botton,width=width_botton, command=an)
    button_ring.place(x=445,y=450)

    img_layers=ImageTk.PhotoImage(Image.open(path7))
    layer=tkinter.Label(root,image=img_layers,height=height_image,width=width_image)
    layer.place(x=241,y=500)
    button_layers=tkinter.Button(root,text='LAYERS METHOD',height=height_botton,width=width_botton, command=ca)
    button_layers.place(x=235,y=700)

   
    root.mainloop()

def cu():
    cubo.create_frame()

def es():
    esfera.create_frame()

def ci():
    cilindro.create_frame()

def pi():
    piramide.create_frame()

def co():
    cono.create_frame()

def an():
    anillos.create_frame()

def ca():
    capas.create_frame()