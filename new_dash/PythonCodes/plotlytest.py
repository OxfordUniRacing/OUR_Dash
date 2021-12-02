from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import webbrowser
import pygal
import glenn01_support

def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))
image_file = resource_path("speedo_bod2.png")
image = tk.PhotoImage(file=image_file)

canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()


def vp_start_gui():
    
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    glenn01_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    glenn01_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
g = 0

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        fname =file=resource_path("speedo_bod2.png")
        bg_image = tk.PhotoImage(file=fname)
        self.Canvas1 = tk.Canvas(top)
        startframe = tk.Frame(root)
        tk.Canvas(startframe, width=2000, height=1500)
        startframe.pack()
        self.Canvas1.pack(expand=YES, fill=BOTH)


        #Screen geometry
        root.bg_image = bg_image
        self.Canvas1.create_image((0, 0), image=root.bg_image, anchor='nw')
        w = bg_image.width()
        h = bg_image.height()
        top.geometry('%dx%d+0+10' % (w,h))        
        top.overrideredirect(True)
        top.title("New Toplevel")
        top.configure(background="#000000")
        
        self.Canvas1.place(relx=-0.004, rely=-0.006, relheight=1.016, relwidth=1.003)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=1203)

        #Exit button     
        self.Button1_7 = tk.Button(top, command=root.destroy)
        self.Button1_7.place(relx=0.9, rely=0.014, height=32, width=70)
        self.Button1_7.configure(activebackground="#68AFD5")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#68AFD5")
        self.Button1_7.configure(disabledforeground="#68AFD5")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#68AFD5")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''EXIT''')

        #Current Speed
        currentSpeed = str(123)
        self.Canvas1.create_text(800, 380, fill="#bf3634", text=currentSpeed, font=("Arial Narrow", 100))
        
        #Battery temp
        battTemp = str(24)
        self.Canvas1.create_text(85, 110, fill="#bf3634", text=battTemp, font=("Arial Narrow", 85))
        #Motor temp
        motorTemp = str(65)
        self.Canvas1.create_text(330, 110, fill="#bf3634", text=motorTemp, font=("Arial Narrow", 85))

        #Battery charge
        battery = 3             #Battery charge

        
        if battery == 3:        #Set the individual states of the images
            state1 = 'normal'
            state2 = 'hidden'
            state3 = 'hidden'
            state4 = 'hidden'
        if battery == 2:
            state2 = 'normal'
            state3 = 'hidden'
            state1 = 'hidden'
            state4 = 'hidden'
        if battery == 1:
            state3 = 'normal'
            state1 = 'hidden'
            state2 = 'hidden'
            state4 = 'hidden'
        if battery == 0:
            state3 = 'hidden'
            state1 = 'hidden'
            state2 = 'hidden'
            state4 = 'normal'

        # Loading the images        
        self.batt_full = tk.PhotoImage(file='Batt_full.png')
        self.batt_2thirds = tk.PhotoImage(file='Batt_2thirds.png')
        self.batt_1third = tk.PhotoImage(file='Batt_1third.png')
        self.batt_dead = tk.PhotoImage(file='Batt_dead.png')
        # Putting the images on the canvas
        self.Canvas1.create_image(172,187, image=self.batt_full, anchor='sw', state=state1)
        self.Canvas1.create_image(172,187, image=self.batt_2thirds, anchor='sw', state=state2)
        self.Canvas1.create_image(172,187, image=self.batt_1third, anchor='sw', state=state3)
        self.Canvas1.create_image(172,187, image=self.batt_dead, anchor='sw', state=state4)

        #Other symbols

        #Scale
        
if __name__ == '__main__':

    vp_start_gui()
