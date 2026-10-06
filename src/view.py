from model import *
from tkinter import *

def to_canvas_coords(canvas, u):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    v = (height / 20) * u
    v *= Vector(1, -1)
    v += Vector(width / 2, height / 2)

    return v

root = Tk()

canvas = Canvas(root, bg="white", width = 800, height = 600)
canvas.pack()

p1 = to_canvas_coords(canvas, Vector(-2.5,-2.5))
p2 = to_canvas_coords(canvas, Vector(2.5,2.5))

print(p1, " : ", p2)

o = canvas.create_oval(p1.x - 0.05, p1.y - 0.05, p1.x + 0.05, p1.y + 0.05, fill="blue")
o = canvas.create_oval(p2.x - 0.05, p2.y - 0.05, p2.x + 0.05, p2.y + 0.05, fill="blue")

_ = input()
