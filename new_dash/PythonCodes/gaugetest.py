import tkinter as tk
#import PIL
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=100, height=100)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                50, 50, image=tkimage)
            self.master.after(100, self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360

root = tk.Tk()
app = SimpleApp(root, 'deg_0.png')
root.mainloop()


