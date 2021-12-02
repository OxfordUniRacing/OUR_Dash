import tkinter as tk
import time
from PIL import ImageTk, Image
# only for input testing
from pynput.keyboard import Key, Listener

# create the main window
window = tk.Tk()
# to rename the title of the window
window.title("Start_Up_Procedure")
# size of window = size of screen
window.geometry("480x272")
window.configure(background='black')
# canvas for animation
canvas_startanim = tk.Canvas(window, width=480, height=272, bg='black')
canvas_startanim.pack()

# Global vars
xspeed = 30 #speed of initial anim car 7
yspeed = 0

# Create start animation of OUR car
def start_anim():
    start_image_load = Image.open("UniLogo.png")
    start_image_load = start_image_load.resize((300,176),Image.ANTIALIAS)
    img_logo = ImageTk.PhotoImage(start_image_load)
    OUR = canvas_startanim.create_image(0,130, image=img_logo)
    anim_loop = True
    while anim_loop == True:
        canvas_startanim.move(OUR, xspeed, yspeed)
        pos_car = canvas_startanim.coords(OUR)
        
        if pos_car[0]>=630:
            #Stop the loop once the car has gone off and delete the car
             anim_loop = False
             canvas_startanim.delete("all")
             canvas_startanim.destroy()
        window.update()
        time.sleep(0.05)
        
def welcome_instructions():
    welcome_l = tk.Label(window, text="Welcome", bg = "black", fg = 'white', font = ("Cherry", 80, "bold"))
    welcome_l.place(x=60,y=70)
    window.update()
    time.sleep(1.3)
    welcome_l.destroy()
    show_instructions(96,120,"   Start-Up Procedure",20,3,tk.LEFT, 'black')
    show_instructions(96,120,"Follow the instructions",20,3,tk.LEFT, 'black')
    window.configure(background="#%02x%02x%02x" % tuple((141, 198, 63)))
    gscree_label = background="#%02x%02x%02x" % tuple((141, 198, 63))
    show_instructions(96,80,"""    Screen will go
    GREEN
    if you complete
    the task""",20,4, tk.CENTER,gscree_label)
    window.configure(background="#%02x%02x%02x" % tuple((190, 57, 57)))
    rscree_label = background="#%02x%02x%02x" % tuple((190, 57, 57))
    show_instructions(96,80,"""    Screen will go
    RED
    if you take
    too long""",20,4, tk.CENTER,rscree_label)
    window.configure(background="#%02x%02x%02x" % tuple((92, 168, 185)))
    bscree_label = background="#%02x%02x%02x" % tuple((92, 168, 185))
    show_instructions(80,110,"""          Ready?
    Checkup Starts Now""",20,3,tk.LEFT, bscree_label)

def check_up():
    show_setup(60,80,"Press Button 1",40,background="#%02x%02x%02x" % tuple((92, 168, 185)))
    
    
def show_setup(xpos,ypos,text_disp,f_size, background):
    inst = tk.Label(window, text=text_disp, bg = background, fg = 'white', font = ("Cherry", f_size, "bold"))
    inst.place(x=xpos,y=ypos)
    window.update()
    terminate_time = 30
    count = 0
    
    while count <= terminate_time:
        print(count)
        def on_press(key):
            print('{0} pressed'.format(
            key))
            if key == Key.cmd:
                count = 100;
    # Collect events until released
        with Listener(
            on_press=on_press) as listener:
            listener.join()
        window.update()
        time.sleep(1)
        count = count+1
        
    if count == 100:
        window.configure(background="#%02x%02x%02x" % tuple((190, 57, 57)))
    
    #time.sleep(sleep_time)
    inst.destroy()    
            
def show_instructions(xpos,ypos,text_disp,f_size,sleep_time, just, background):
    inst = tk.Label(window, text=text_disp, justify = just, bg = background, fg = 'white', font = ("Cherry", f_size, "bold"))
    inst.place(x=xpos,y=ypos)
    window.update()
    time.sleep(sleep_time)
    inst.destroy()
            
            
    
start_anim()
welcome_instructions()
check_up()
window.mainloop()
