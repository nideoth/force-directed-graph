import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim

from algorithm import algorithm_frames


def display_final(vertices, edges, iterations, width, height):
    result = algorithm_frames(vertices, edges, iterations, width, height)[iterations-1]

    graph = nx.Graph()

    # Add nodes
    for i, node in enumerate(result):
        graph.add_node(i, pos=(node.pos.x, node.pos.y))

    # Add edges
    for edge in edges:
        graph.add_edge(edge.u, edge.v)
        
    nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True)
    plt.show()


def display_animated(vertices, edges, iterations, width, height):

    def update(num, graph, ax, result_frames):
        ax.clear()
        graph = nx.Graph()

        ax.set_title(f"Iteration: {num+1}")

        # Add nodes
        for i, node in enumerate(result_frames[num]):
            graph.add_node(i, pos=(node.pos.x, node.pos.y))

        # Add edges
        for edge in edges:
            graph.add_edge(edge.u, edge.v)

        nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True)

    def init():

        result_frames = algorithm_frames(vertices, edges, iterations, width, height)

        fig, ax = plt.subplots()
        graph = nx.Graph()
        ani = anim.FuncAnimation(fig, update, frames=iterations, fargs=(graph, ax, result_frames), repeat=False, interval=10)
        plt.show()

    init()
