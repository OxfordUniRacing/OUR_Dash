from tkinter import *
import time
import os
root = Tk()

frameCnt = 80
frames = [PhotoImage(file=r"C:\Users\Gebruiker\AppData\Local\Programs\Python\Python39\PythonCodes\OURlogo.gif", format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(10, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
