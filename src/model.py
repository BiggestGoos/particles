
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        f'({self.x}, {self.y})'

    def __rmul__(self, factor):
        return Vector(self.x * factor, self.y * factor)
