from tkinter import *

root = Tk()

canvas = Canvas(root, bg="white", width = 800, height = 600)

o = canvas.create_oval(80, 30, 140, 150, fill="blue")

input()