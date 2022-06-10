import networkx as nx
import matplotlib.pyplot as plt

from algorithm import Edge, algorithm


if __name__ == "__main__":

    edges = [
        Edge(u=0, v=1),
        Edge(u=1, v=2),
        Edge(u=2, v=3),
        Edge(u=3, v=0),

        Edge(u=0, v=2),
        Edge(u=1, v=3),
    ]

    result = algorithm(edges, 4, 100)

    for i in result:
        print(i.pos.x, i.pos.y)

    graph = nx.Graph()

    # Add nodes
    for i, node in enumerate(result):
        graph.add_node(i, pos=(node.pos.x, node.pos.y))

    # Add edges
    for edge in edges:
        graph.add_edge(edge.u, edge.v)
    
    nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True)
    plt.show()
