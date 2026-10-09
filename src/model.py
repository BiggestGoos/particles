class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __rmul__(self, factor):
        return Vec(self.x * factor, self.y * factor)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def vec_mul(self, other):
        return Vec(self.x * other.x, self.y * other.y)

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
        self.position += dt * self.velocity

    def apply_force(self, dt, f: Vec):
        acc = (self.mass ** -1) * f
        self.velocity += dt * acc

    def bounding_box(self):
        r = self.radius
        p = self.position
        corner_v = Vec(r,-r)
        return p-corner_v, p+corner_v
