import igraph as ig
import matplotlib.pyplot as plt
import random

random.seed(0)
# g = ig.Graph.GRG(50, 0.15)
# createan empty graph
g = ig.Graph()
# add four five vertices to the graph by name of 0 to 4
g.add_vertices(5)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
# and some random edges between these four vertices
g.add_edges([
    (0, 2),
    (2, 4),
    (4, 0),
    (1, 3)
])

# how many vertices are there in this graph
print(g.vcount())

# how many edges are there in this graph
print(g.ecount())

# get the adjacency matrix of the graph
print(g.get_adjacency())

# get the degree of each vertex
print(g.degree())

# get the degree of vertex 2
print(g.degree(2))





