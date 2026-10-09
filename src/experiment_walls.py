from view import *
import math

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u
    particles.append(Particle(1,pos,vel,0.2))

lower = -10
higher = 10

def test_particle(k, particle):
    r = particle.radius
    x = particle.position.x
    y = particle.position.y

    low_x = lower - (x - r)
    high_x = (x + r) - higher

    low_y = lower - (y - r)
    high_y = (y + r) - higher

    if (low_x > 0): # Left wall
        yield Vec(k * low_x, 0)

    if (high_x > 0): # Right wall
        yield Vec(-(k * high_x), 0)

    if (low_y > 0): # Bottom wall
        yield Vec(0, k * low_y)

    if (high_y > 0): # Top wall
        yield Vec(0, -(k * high_y))

def walls(dt,particles):
    k = 5

    for particle in particles:
        for force in test_particle(k, particle):
            particle.apply_force(dt, force)

simulation_loop(walls, 0.0016, particles)
