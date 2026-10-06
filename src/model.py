class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __rmul__(self, factor):
        return Vector(self.x * factor, self.y * factor)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_chords(self):
        return self.x, self.y

def dot(u, v):
    return u.x * v.x + u.y * v.y

class Particle:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius

    def intertial_move(self, dt):
        self.position += self.velocity * dt

    def apply_force(self, dt, f):
        acc = f * self.mass ** -1
        self.velocity += acc * dt
