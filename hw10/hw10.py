import os
import random
from tkinter import *

def buttonPressed( event ):
   f = random.randrange(8)
   os.system("afplay ./"+str(f)+".wav")

canvas_width = 500
canvas_height =400
python_green = "#476042"

master = Tk()
master.title("abady ")

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/2, 100, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/2, 200, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/2, 300, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/2, 500, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/3, 800, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/3, 1000, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)
points = [0,0,canvas_width,canvas_height/3, 1500, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

w.bind( "<Button-1>", buttonPressed )

mainloop()