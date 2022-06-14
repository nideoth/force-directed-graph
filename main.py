from random import randint
import sys

from algorithm import Vector, Vertex, Edge
from display import display_animated, display_final


if __name__ == "__main__":

    WIDTH = 100
    HEIGHT = 100
    ANIMATION = True

    if len(sys.argv) >= 3:
        file = sys.argv[1]
        number_of_iterations = int(sys.argv[2])
    else:
        print("Bad arguments")
        exit()

    file = open(file, "r")
    edges_list = []
    max_value = 0
    for line in file:
        stripped_line = line.strip()
        coordinates = stripped_line.split()
        u = int(coordinates[0])
        v = int(coordinates[1])
        edges_list.append(Edge(u, v))
        if max_value < max(u, v):
            max_value = max(u, v)
    file.close()

    vertices = []
    for _ in range(max_value+1):
        vertices.append(Vertex(Vector(randint(-WIDTH//2, WIDTH//2), randint(-HEIGHT//2, HEIGHT//2))))


    if ANIMATION:
        display_animated(vertices, edges_list, number_of_iterations, WIDTH, HEIGHT)
    else:
        display_final(vertices, edges_list, number_of_iterations, WIDTH, HEIGHT)
