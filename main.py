from random import randint

from algorithm import Vector, Vertex, Edge
from display import display_animated, display_final


if __name__ == "__main__":

    WIDTH = 100
    HEIGHT = 100
    ITERATIONS = 300
    ANIMATION = True

    edges = [
        Edge(u=0, v=1),
        Edge(u=1, v=2),
        Edge(u=2, v=3),
        Edge(u=3, v=0),

        Edge(u=0, v=4),
        Edge(u=1, v=5),
        Edge(u=2, v=6),
        Edge(u=3, v=7),
    ]

    vertices = []
    for _ in range(8):
        vertices.append(Vertex(Vector(randint(-WIDTH//2, WIDTH//2), randint(-HEIGHT//2, HEIGHT//2))))


    if ANIMATION:
        display_animated(vertices, edges, ITERATIONS, WIDTH, HEIGHT)
    else:
        display_final(vertices, edges, ITERATIONS, WIDTH, HEIGHT)
