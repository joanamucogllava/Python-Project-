"""
This collection of functions are used to create a MST
using Prim's algorithim

"""


# Determines the total weight of a graph
def cost(graph, e):
    return graph.edges()[e]['weight']


# This function is important in creating the MST
def valid_incident_edges(graph, tree):
    
    # Initilize a list of edge sets in T after each iteration
    edges = []
    for e in graph.edges():
        if (e[0] in tree.nodes() or e[1] in tree.nodes()):
            # Appends all sets of edges with nodes in subgraph T
            edges.append(e)
    
    # Used to output a list of viable edge sets for the next node iteration
    valid_edges = []
    for v in edges:
        
        #remove the edge sets that would create a cycle
        if not((v[0] in tree.nodes()) and (v[1] in tree.nodes())):
            valid_edges.append(v)
    
    return valid_edges


# Will output the lowest cost weight edge to add to the subgraph T
def min_possible_prims_edge(graph, tree):
    possible_e = valid_incident_edges(graph, tree)
    min_e = possible_e[0]
    
    # Iterate through the available edges and choose the lowest cost edge
    for e in possible_e:
        if cost(graph, e) < cost(graph, min_e):
            min_e = e
    return min_e

