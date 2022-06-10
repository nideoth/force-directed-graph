from math import sqrt
from random import randint


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other)
    def __truediv__(self, other: int):
        return Vector(self.x / other, self.y / other)
    def __floordiv__(self, other: int):
        return Vector(self.x // other, self.y // other)
    def __abs__(self):
        return round(sqrt(self.x**2 + self.y**2))
    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))


class Vertex:
    def __init__(self, pos: Vector):
        self.pos = pos
        self.disp = Vector(0, 0)


class Edge:
    def __init__(self, v: int, u: int):
        self.v = v
        self.u = u
        

WIDTH = 100
HEIGHT = 100
AREA = WIDTH * HEIGHT
INIT_TEMP = WIDTH // 10


def algorithm(edges: list[Edge], vertices_count: int, iterations: int) -> list[Vertex]:

    # Vertices are assigned random initial positions
    vertices = []
    for _ in range(vertices_count):
        vertices.append(Vertex(Vector(randint(-WIDTH//2, WIDTH//2), randint(-HEIGHT//2, HEIGHT//2))))

    K = sqrt(AREA / len(vertices))

    def fa(x: float) -> float:
        return (x**2) / K

    def fr(x: float) -> float:
        return (K**2) / x

    temperature = INIT_TEMP

    for _ in range(iterations):
        # Calculate repulsive forces
        for v in vertices:
            v.disp = Vector(0, 0)
            for u in vertices:
                if not u == v:
                    delta = v.pos - u.pos
                    if abs(delta) == 0: continue
                    v.disp += ((delta/abs(delta)) * fr(abs(delta)))

        # Calculate attractive forces
        for e in edges:
            delta = vertices[e.v].pos - vertices[e.u].pos
            if abs(delta) == 0: continue
            vertices[e.v].disp -= ((delta/abs(delta)) * fa(abs(delta)))
            vertices[e.u].disp += ((delta/abs(delta)) * fa(abs(delta)))

        # Limit the maximum displacement to the temperature
        # Prevent from being displaced outside frame
        for v in vertices:
            if abs(v.disp) != 0:
                v.pos += ((v.disp/abs(v.disp)) * min(abs(v.disp), temperature))
            v.pos.x = min(WIDTH//2, max(-WIDTH/2, v.pos.x))
            v.pos.y = min(HEIGHT//2, max(-HEIGHT/2, v.pos.y))

        # Decay temperature to 0 in an inverse linear fashion
        temperature -= (INIT_TEMP / iterations)

    return vertices
