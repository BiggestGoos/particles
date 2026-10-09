from model import *
from tkinter import *

def to_canvas_coords(canvas, u):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    v = (height / 20) * u
    v = v.vec_mul(Vec(1, -1))
    v += Vec(width / 2, height / 2)

    return v

def bounding_box_to_canvas_coords(canvas, bounding_box):
    return (to_canvas_coords(canvas, bounding_box[0]), to_canvas_coords(canvas, bounding_box[1]))

def move_oval_to(canvas, oval, u1, u2):
    v1, v2 = bounding_box_to_canvas_coords(canvas, (u1, u2))
    canvas.coords(oval, v1.x, v1.y, v2.x, v2.y)

def create_oval(canvas, particle):
    v1, v2 = bounding_box_to_canvas_coords(canvas, particle.bounding_box())
    return canvas.create_oval(v1.x, v1.y, v2.x, v2.y, fill="blue")

root = Tk()

canvas = Canvas(root, bg="white", width = 800, height = 600)
canvas.pack()


# particle1 = Particle(1,Vector(0,0),Vector(0,0),2)

# o = create_oval(canvas, particle1)

def simulation_loop(f, timestep, particles):

    particle_pairs = []

    for p in particles:
        particle_pairs.append([create_oval(canvas, p), p])

    while True:
        f(timestep, particles)
        for p in particle_pairs:
            p[1].intertial_move(timestep)

            move_oval_to(canvas, p[0], *p[1].bounding_box())

        canvas.update()
