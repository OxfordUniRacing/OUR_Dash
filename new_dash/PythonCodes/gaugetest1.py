from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import webbrowser
import pygal
import csv
import glenn01_support
from PIL import ImageTk
from PIL import Image, ImageSequence

def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#root = tk.Tk()
#root.overrideredirect(True)
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
#root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))
#image_file = resource_path("speedo_bod2.png")
#image = tk.PhotoImage(file=image_file)

#canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
#canvas.create_image(width*0.5/2, height*0.5/2, image=image)
#canvas.pack()
#root.after(5000, root.destroy)
#root.mainloop()
global index
index = 0

def update(top):
    global index
    index += 1
    top.dataUpdate(index)
    root.after(1,update,top)

def vp_start_gui():
    
    global val, w, root
    
    root = tk.Tk()
    top = Toplevel1 (root)
    glenn01_support.init(root, top)

    update(top)
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
    
    def dataUpdate(self, index):
        with open('TestFile.csv') as data_file:
            csv_read = csv.reader(data_file, delimiter=',')

            self.csv_reader = []
            for row in csv_read:
                self.csv_reader.append(float(row[index]))
           
        self.speedUpdate()
        self.battUpdate()
        self.motorTempUpdate()
        self.voltageUpdate()
        self.pedalUpdate()
        self.sensorUpdate()
        self.CANUpdate()
        self.battCUpdate()
        self.battVUpdate()
        self.waterUpdate()

        self.gifUpdate(index)

    def gifUpdate(self, index):
        
        # Find index of gif frame
        gif = index % 84

        print(85 % 84)
        
        self.Canvas1.delete(self.gif_id)
        self.gif_id = self.Canvas1.create_image(25, 520, image=self.image_gif[gif], anchor= 'sw', state='normal')


    def speedUpdate(self):

        #Reset 
        self.Canvas1.delete(self.currentSpeed_id)

        # Get and set new
        self.currentSpeed = self.csv_reader[0]     
        self.currentSpeed_id = self.Canvas1.create_text(678, 310, fill="#bf3634", text=str(round(self.currentSpeed, 1)), font=("Arial Narrow", 80))

        # 323.5 deg is at 0 and 36.5 deg is at 190, so 8 deg = 5 kph       
        angle = 323.5 - self.currentSpeed*(323.5-36.5)/190
        #angle = 180
        self.rotated=self.arrow.rotate(angle)
        self.rotated.save('arrowR.png')
        self.filenameRot = 'arrowR.png'
        
        self.Canvas1.delete(self.arrowIm_id)
        self.arrowIm = tk.PhotoImage(file = self.filenameRot)
        self.arrowIm_id = self.Canvas1.create_image(445,520, image=self.arrowIm, anchor='sw', state='normal')

    def battUpdate(self):

        #Reset
        self.Canvas1.delete(self.battTemp_id)

        #Get and set new
        self.battTemp = int(self.csv_reader[1])
        self.battTemp_id = self.Canvas1.create_text(73, 88, fill="#bf3634", text=str(self.battTemp), font=("Arial Narrow", 63))

    def motorTempUpdate(self):

        #Reset
        self.Canvas1.delete(self.motorTemp_id)

        #New
        self.motorTemp = int(self.csv_reader[2])
        self.motorTemp_id = self.Canvas1.create_text(280, 88, fill="#bf3634", text=str(self.motorTemp), font=("Arial Narrow", 63))

    def voltageUpdate(self):

        indexUpdate = self.csv_reader[3]
        self.Canvas1.delete(self.voltage_id)
        
        if indexUpdate == 1 : self.voltage_id = self.Canvas1.create_image(130,330, image=self.voltage_grey, anchor='sw', state='normal')
        if indexUpdate == 2 : self.voltage_id = self.Canvas1.create_image(130,330, image=self.voltage_red, anchor='sw', state='normal')
        if indexUpdate == 3 : self.voltage_id = self.Canvas1.create_image(130,330, image=self.voltage_yellow, anchor='sw', state='normal')

    def pedalUpdate(self):

        indexUpdate = self.csv_reader[4]
        self.Canvas1.delete(self.pedal_id)

        if indexUpdate == 1 : self.pedal_id = self.Canvas1.create_image(250,260, image=self.pedal_grey, anchor='sw', state='normal')
        if indexUpdate == 2 : self.pedal_id = self.Canvas1.create_image(250,260, image=self.pedal_red, anchor='sw', state='normal')

    def sensorUpdate(self):
        
        indexUpdate = self.csv_reader[5]
        self.Canvas1.delete(self.sensor_id)

        if self.sensor_id == 1 : self.sensor_id = self.Canvas1.create_image(25,400, image=self.sensor_grey, anchor='sw', state='normal')
        if self.sensor_id == 2 : self.sensor_id = self.Canvas1.create_image(25,400, image=self.sensor_red, anchor='sw', state='normal')
        if self.sensor_id == 3 : self.sensor_id = self.Canvas1.create_image(25,400, image=self.sensor_yellow, anchor='sw', state='normal')

    def CANUpdate(self):

        indexUpdate = self.csv_reader[6]
        self.Canvas1.delete(self.CAN_id)

        if indexUpdate == 1: self.CAN_id = self.Canvas1.create_image(130,260, image=self.CAN_grey, anchor='sw', state='normal')
        if indexUpdate == 2: self.CAN_id = self.Canvas1.create_image(130,260, image=self.CAN_red, anchor='sw', state='normal')
        if indexUpdate == 3: self.CAN_id = self.Canvas1.create_image(130,260, image=self.CAN_yellow, anchor='sw', state='normal')

    def battCUpdate(self):

        indexUpdate = self.csv_reader[7]
        self.Canvas1.delete(self.battC_id)
        
        if indexUpdate == 0: self.battC_id = self.Canvas1.create_image(147,155, image=self.batt_full, anchor='sw', state='normal')
        if indexUpdate == 1: self.battC_id = self.Canvas1.create_image(147,155, image=self.batt_2thirds, anchor='sw', state='normal')
        if indexUpdate == 2: self.battC_id = self.Canvas1.create_image(147,155, image=self.batt_1third, anchor='sw', state='normal')
        if indexUpdate == 3: self.battC_id = self.Canvas1.create_image(147,155, image=self.batt_dead, anchor='sw', state='normal')

    def battVUpdate(self):

        indexUpdate = self.csv_reader[8]
        self.Canvas1.delete(self.battV_id)

        if indexUpdate == 1: self.battV_id = self.Canvas1.create_image(25,260, image=self.batt_12v_grey, anchor='sw', state='normal')
        if indexUpdate == 2: self.battV_id = self.Canvas1.create_image(25,260, image=self.batt_12v_red, anchor='sw', state='normal')

    def waterUpdate(self):

        indexUpdate = self.csv_reader[9]
        self.Canvas1.delete(self.water_id)

        if indexUpdate == 1: self.water_id = self.Canvas1.create_image(25,330, image=self.water_level_grey, anchor='sw', state='normal')
        if indexUpdate == 2: self.water_id = self.Canvas1.create_image(25,330, image=self.water_level_red, anchor='sw', state='normal')

    def split_animated_gif(self, gif_file_path):
        
        im = Image.open(gif_file_path)
        self.image_gif = []
        
        index = 0
        for frame in ImageSequence.Iterator(im):
            frame.save(r'frame%d.png' % index)  
            index += 1
            print(index)

        for i in range(84):
            self.image_gif.append(tk.PhotoImage(file=('frame%d.png' % i)))
            print(i)
        

    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        fname =file=resource_path("speedo_bod3.png")
        bg_image = tk.PhotoImage(file=fname)
        self.Canvas1 = tk.Canvas(top)
        startframe = tk.Frame(root)
        tk.Canvas(startframe, width=bg_image.width()*0.5, height=bg_image.height()*0.5)
        startframe.pack()
        self.Canvas1.pack(expand=YES, fill=BOTH)

        #Screen geometry
        root.bg_image = bg_image
        # location of the speedometer
        self.Canvas1.create_image((0, 0), image=bg_image, anchor='nw')
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
        self.currentSpeed = 0
        self.currentSpeed_id = self.Canvas1.create_text(688, 315, fill="#bf3634", text=str(self.currentSpeed), font=("Arial Narrow", 80))
        
        #Battery temp
        self.battTemp = 0
        self.battTemp_id = self.Canvas1.create_text(73, 88, fill="#bf3634", text=str(self.battTemp), font=("Arial Narrow", 63))

        #Motor temp
        self.motorTemp = 0
        self.motorTemp_id = self.Canvas1.create_text(280, 88, fill="#bf3634", text=str(self.motorTemp), font=("Arial Narrow", 63))

        #Battery charge
        self.batt_full = tk.PhotoImage(file='Batt_full.png')
        self.batt_2thirds = tk.PhotoImage(file='Batt_2thirds.png')
        self.batt_1third = tk.PhotoImage(file='Batt_1third.png')
        self.batt_dead = tk.PhotoImage(file='Batt_dead.png')

        self.battC_id = self.Canvas1.create_image(147,155, image=self.batt_dead, anchor='sw', state='normal')

        #CAN - define state
        self.CAN_grey = tk.PhotoImage(file='CAN_grey.png')
        self.CAN_red = tk.PhotoImage(file='CAN_red.png')
        self.CAN_yellow = tk.PhotoImage(file='CAN_yellow.png')

        self.CAN_id = self.Canvas1.create_image(130,260, image=self.CAN_red, anchor='sw', state='normal')

        #Batv - define state
        self.batt_12v_grey = tk.PhotoImage(file='Batt_12v_grey.png')
        self.batt_12v_red = tk.PhotoImage(file='Batt_12v_red.png')

        self.battV_id = self.Canvas1.create_image(25,260, image=self.batt_12v_red, anchor='sw', state='normal')

        #Water level - define state
        self.water_level_grey = tk.PhotoImage(file='Water_Level_grey.png')
        self.water_level_red = tk.PhotoImage(file='Water_Level_red.png')

        self.water_id = self.Canvas1.create_image(25,330, image=self.water_level_red, anchor='sw', state='normal')
        
        #Voltage - define state
        self.voltage_grey = tk.PhotoImage(file='Voltage_grey.png')
        self.voltage_red = tk.PhotoImage(file='Voltage_red.png')
        self.voltage_yellow = tk.PhotoImage(file='Voltage_yellow.png')

        self.voltage_id = self.Canvas1.create_image(130,330, image=self.voltage_red, anchor='sw', state='normal')

        #Sensor - define state
        self.sensor_grey = tk.PhotoImage(file='Sensor_grey.png')
        self.sensor_red = tk.PhotoImage(file='Sensor_red.png')
        self.sensor_yellow = tk.PhotoImage(file='Sensor_yellow.png')

        self.sensor_id = self.Canvas1.create_image(25,400, image=self.sensor_red, anchor='sw', state='normal')
        
        #Pedal - define state
        self.pedal_grey = tk.PhotoImage(file='Pedal_grey.png')
        self.pedal_red = tk.PhotoImage(file='Pedal_red.png')

        self.pedal_id = self.Canvas1.create_image(250,260, image=self.pedal_red, anchor='sw', state='normal')

        #Scale
        self.filename = 'arrow1.png'
        self.arrow = Image.open(self.filename)

        # 323.5 deg is at 0 and 37.25 deg is at 190, so 8 deg = 5 kph
        angle = 323.5 - int(self.currentSpeed)*(323.5-37.25)/190   
        self.rotated=self.arrow.rotate(angle)
        self.rotated.save('arrowR.png')
        self.filenameRot = 'arrowR.png'
        
        self.arrowIm = tk.PhotoImage(file = self.filenameRot)
        self.arrowIm_id = self.Canvas1.create_image(500,0, image=self.arrowIm, anchor='se', state='normal')

        #GIF
        self.split_animated_gif(r'C:\Users\Gebruiker\AppData\Local\Programs\Python\Python39\PythonCodes\OURlogo1.gif')       
        self.gif_id = self.Canvas1.create_image(100, 100, image=self.image_gif[0], anchor= 'ne', state='normal')
        
               
if __name__ == '__main__':

    vp_start_gui()
