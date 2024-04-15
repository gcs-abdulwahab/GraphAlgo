import igraph as ig
import matplotlib.pyplot as plt
import random

random.seed(0)
# g = ig.Graph.GRG(50, 0.15)
# createan empty graph
g = ig.Graph()
# add four five vertices to the graph by name of 0 to 4
g.add_vertices(16)

g.vs["name"] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

# add some edges to the graph in the above 16 vertices
#  add edges between sixteen vertices in the graph
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#  A B C D E F G H I J K  L  M  N  O  P
# using range function to add random edges between vertices

for i in range(0, 16):
    g.add_edge(i, random.randint(0, 15))


# add an edge between vertic O and A
g.add_edge(14, 0)

# add random weights to the edges but they should not be repeated
weights = []
for i in range(0, g.ecount()):
    weights.append(random.randint(1, 10))


# # how many vertices are there in this graph
# print(g.vcount())
#
# # how many edges are there in this graph
# print(g.ecount())

# get the adjacency matrix of the graph it should show the weights of the edges
print(g.get_adjacency())


# get the degree of each vertex
print(g.degree())

# # get the degree of vertex 2
# print(g.degree(2))

# # get the neighbors of vertex 2
# print(g.neighbors(2))


# # is this graph connected
# print(g.is_connected())

# get the MST of the graph
#  how many msts can be made from the graph

# run the mst but such that it keeps the original weight of the edge in the graph
mst = g.spanning_tree()

#  run BFS first traversal  on the graph starting form vertix A
# dfs = g.depth_first_search(0)

#  visualize the graph using matplotlib

components = g.connected_components(mode='weak')

fig, ax = plt.subplots()
visual_style = {}
visual_style["vertex_size"] = 7
visual_style["vertex_color"] = list(map(int, ig.rescale(components.membership, (0, 200), clamp=True)))
visual_style["edge_width"] = 0.7
visual_style["vertex_label"] = g.vs["name"]
visual_style["vertex_label_size"] = 20  # Set the font size to 20

ig.plot(components, target=ax, palette=ig.RainbowPalette(), **visual_style)
plt.show()
