import networkx as nx
G = nx.Graph()

# Adding nodes
G.add_node(1) # add a node
G.add_nodes_from([2,3]) # add a list of nodes
H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

# Adding edges
#single
G.add_edge(1,2)
e = (2,3)
G.add_edge(*e)

#list
G.add_edges_from([(1,2), (1,3)])

#Note:
# or by adding any ebunch of edges.
# An ebunch is any iterable container of edge-tuples.
# An edge-tuple can be a 2-tuple of nodes or a 3-tuple with 2 nodes followed by an edge attribute dictionary, e.g. (2,3,{‘weight’:3.1415}).
# Edge attributes are discussed further below
#
# >>> G.add_edges_from(H.edges())
# One can demolish the graph in a similar fashion;
# using Graph.remove_node(), Graph.remove_nodes_from(),
# Graph.remove_edge() and Graph.remove_edges_from(), e.g. >>> G.remove_node(H)

print("Nodes: " + str(G.nodes()))
print("Edges: " + str(G.edges()))

